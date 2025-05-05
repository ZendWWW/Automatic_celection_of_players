from django.contrib import admin
from .models import Service, Request, RequestService

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'price', 'image_url', 'status')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'creator', 'created_at', 'total_amount')
    list_filter = ('status',)
    raw_id_fields = ('creator', 'moderator')

@admin.register(RequestService)
class RequestServiceAdmin(admin.ModelAdmin):
    list_display = ('request', 'service', 'quantity')
    raw_id_fields = ('request', 'service')