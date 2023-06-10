from django.urls import path

from chat_app import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('otp/',views.ConfirmOTPView.as_view()),
    path('login/', views.LoginView.as_view()),

]
