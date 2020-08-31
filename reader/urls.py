from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/', views.search_page, name='search_page'),
    path('manga/<str:manga_name>', views.manga_page, name='manga_page'),
    path('manga/<str:manga_name>/<str:chapter>', views.chapter_page, name='chapter_page')
]