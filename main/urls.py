from django.urls import path
from . import views
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    #path('', views.base, name='base'),
    path('servises/', views.Map_selection_page, name='Map_selection_page'),
]
