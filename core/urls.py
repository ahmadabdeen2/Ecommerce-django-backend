from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import get_my_details

router = DefaultRouter()

router.register(r'users', ProfileViewSet)

urlpatterns = [
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   path('get_my_details/', get_my_details, name='get_my_details'),
] + router.urls