from django.urls import path
from . import views
urlpatterns = [
    #path('', views.base, name='base'),
    path('servises/', views.Map_selection_page, name='Map_selection_page'),

]
