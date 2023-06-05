from rest_framework import serializers

from chat_app.models import User, Request, Chat, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email_address', 'username', 'password',
                  'profile_picture', 'last_seen', 'request', 'notification']


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
