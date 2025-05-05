from django.db import models
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q

class Service(models.Model):
    STATUS_CHOICES = [
        ('active', 'Действует'),
        ('deleted', 'Удалена'),
    ]

    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='active')
    image_url = models.URLField('URL изображения', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class Request(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('deleted', 'Удалена'),
        ('formed', 'Сформирована'),
        ('completed', 'Завершена'),
        ('declined', 'Отклонена'),
    ]

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    formed_at = models.DateTimeField('Дата формирования', null=True, blank=True)
    completed_at = models.DateTimeField('Дата завершения', null=True, blank=True)
    moderator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='moderated_requests')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    total_amount = models.DecimalField('Общая сумма', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        constraints = [
            models.UniqueConstraint(
                fields=['creator'],
                condition=Q(status='draft'),
                name='unique_draft_request_per_user'
            )
        ]

    def __str__(self):
        return f"Заявка #{self.id} ({self.get_status_display()})"

    def update_total_amount(self):
        total = sum(item.service.price * item.quantity for item in self.services.all())
        self.total_amount = total
        self.save()

class RequestService(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='services')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='Услуга')
    quantity = models.PositiveIntegerField('Количество', default=1)
    added_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Услуга в заявке'
        verbose_name_plural = 'Услуги в заявках'
        unique_together = ('request', 'service')

    def __str__(self):
        return f"{self.service.name} x{self.quantity}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.request.update_total_amount()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.request.update_total_amount()
