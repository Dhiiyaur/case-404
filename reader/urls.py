from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/', views.search_page, name='search_page'),
    path('manga/<str:manga_name>', views.manga_page, name='manga_page'),
    path('manga/<str:manga_name>/<str:chapter>', views.chapter_page, name='chapter_page'),

    # IND
    path('ID/search/', views.search_page, name='search_page_id'),
    path('ID/manga/<str:manga_name>', views.ID_manga_page, name='manga_page_id'),
    path('ID/manga/<str:manga_name>/<str:chapter>', views.ID_chapter_page, name='chapter_page_id'),
]