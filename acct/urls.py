from django.urls import path, include
from django.shortcuts import render
from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:account_type>/', views.request_account, name='Create Account Request'),

]
