from rest_framework import serializers

from chat_app.models import Request, Chat, Notification, TempUser

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'initiator_username', 'recipient_username', 'status', 'type', 'time_accepted_or_declined']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['request', 'recipient_username']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'sender_username', 'recipient_username', 'message']


class TempUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempUser
        fields = ['email', 'username', 'password', 'otp']
