from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Map_selection_page, name='home'),
    path('servises/Map_selection_page.html/', views.Map_selection_page, name='Map_selection_page'),
    path("karta_info/<int:map_id>/",views.Map_info_page, name="Map_mirage_info_page"),
    path('servises/Search_for_the_match/', views.search_for_the_match, name='Search_for_the_match'),
    path('search_maps/', views.search_maps, name='search_maps'),
]
