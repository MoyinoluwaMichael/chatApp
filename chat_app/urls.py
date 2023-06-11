from django.urls import path, include
from rest_framework.routers import SimpleRouter

from chat_app import views


urlpatterns = [
    path('register/', views.RegisterUserView.as_view())
]
