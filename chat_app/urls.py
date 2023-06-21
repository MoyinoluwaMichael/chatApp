from django.urls import path, include
from rest_framework.routers import SimpleRouter

from chat_app import views
route = SimpleRouter()
route.register('chatBox', views.AllChatsRoute)

urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('completeRegistration/', views.CompleteRegistration.as_view()),
    path('', include(route.urls))
]
