from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import  RegistrationView, LogoutView

urlpatterns = [
    path('account/register/', RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
]