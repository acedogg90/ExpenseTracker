from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('logout_user', views.logout_user, name='logout'),
    path("login", views.login, name="login"),
    path("register_user", views.register_user, name="register_user"),
    path('chart', views.chart, name='chart'),
    path('add_book', views.add_book, name='add_book'),
    path('book_list', views.book_list, name='book_list'),
]