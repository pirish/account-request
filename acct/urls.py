from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'reqs', views.AccountRequestViewSet)
router.register(r'types', views.AccountTypeViewSet)

urlpatterns = [
    path('new/', views.request_account, name='Create Account Request'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
