from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('page-<str:slug>', views.page),
    path('page_edit-<str:slug>', views.page_edit),
    path('post_page_edit', views.post_page_edit),
]
