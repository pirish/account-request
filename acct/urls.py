from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<string:account_type>/', views.create_request, name='Create Request'),

]
