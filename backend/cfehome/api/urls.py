from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home, name="api-home"),
    path("auth/", obtain_auth_token),
]
