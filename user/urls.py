from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserProfileView

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token'),
    # path('<str:username>/', UserProfileView.as_view(), name='user-profile'),
]