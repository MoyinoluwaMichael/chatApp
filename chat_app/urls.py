from django.urls import path

from chat_app import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view())
]
