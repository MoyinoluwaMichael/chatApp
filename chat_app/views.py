from rest_framework.views import APIView, View
from rest_framework import status
from rest_framework.response import Response

from chat_app.models import User
from chat_app.serializers import UserSerializer


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
