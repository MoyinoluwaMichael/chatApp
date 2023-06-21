import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from chat_app.dtos import RegistrationRequest
from chat_app.models import User, TempUser, Chat
from chat_app.repositories import save_registration_request, find_registration_request_by_email, delete_temp_user
from chat_app.serializers import UserSerializer, TempUserSerializer, ChatSerializer
from chat_app.utils import sendOnboardingMail


def generate_otp():
    return str(random.randint(1000, 9999))


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = request.data.get("otp")
        email: str = request.data.get('email')
        username = request.data.get('username')
        found_temp_user: RegistrationRequest = find_registration_request_by_email(email)
        it_is_a_fresh_registration: bool = otp is None
        if it_is_a_fresh_registration and found_temp_user is None:
            return self.register_user_temporarilly(request)
        elif found_temp_user is not None:
            return Response({'message': f'OTP already sent to user with {email}.'},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def register_user_temporarilly(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        otp = generate_otp()
        temp_user: TempUser = TempUser()
        temp_user.username = username
        temp_user.otp = otp
        temp_user.email = email
        temp_user.password = password
        serializers = TempUserSerializer(data=temp_user.__dict__)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        sendOnboardingMail(username, otp, email)
        return Response({'message': 'Success'},
                        status=status.HTTP_201_CREATED)


class CompleteRegistration(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        temp_user = TempUser.objects.filter(email=email, otp=otp)
        serializer = UserSerializer(data=temp_user[0].__dict__)
        if temp_user.exists():
            serializer.is_valid(raise_exception=True)
            serializer.save()
            temp_user.delete()
            return Response({'message': 'Registration successful'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid OTP code'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = TempUser.objects.all()
        serializer = TempUserSerializer(users, many=True)
        return Response(serializer.data)

    def delete(self, request):
        user = TempUser.objects.all()
        user.delete()
        return Response("Deleted successfully")


class AllChatsRoute(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def list(self, request, *args, **kwargs):
        chats: list[Chat] = Chat.objects.all()
        username: str = request.data.get("username")
        friend_username: str = request.data.get("friendUsername")
        if username == "" or username is None:
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        username = username.lower()
        friend_username = friend_username.lower()
        chat_box: list[Chat] = []
        for chat in chats:
            sender = str(chat.sender_username).lower()
            recipient = str(chat.recipient_username).lower()
            if (sender == username and recipient == friend_username) or (sender == friend_username and recipient == username):
                chat_box.append(chat)
        serializer = ChatSerializer(chat_box, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if request.data.get("username") is not None:
            return self.list(request, *args, **kwargs)
        else:
            return super().create(request, *args, **kwargs)
