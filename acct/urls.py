from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'reqs', views.AccountRequestViewSet)
router.register(r'types', views.AccountTypeViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<str:account_type>/', views.request_account, name='Create Account Request'),

]
