import random
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from chat_app.serializers import UserSerializer

otp = ""


def generate_otp():
    return str(random.randint(1000, 9999))


class RegisterUserView(APIView):
    def post(self, request):
        global otp
        email = request.data.get('email')
        username = request.data.get('username')

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            otp = generate_otp()

            subject = 'Registration Confirmation'
            message = 'Hello {},\n\nThank you for registering. Your account has been created.' \
                      ' Use this OTP {} to verify your account.'.format(username, otp)
            from_email = '7ate9CHAT@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return Response({'message': 'Registration successful. A confirmation email has been sent to your email.'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmOTPView(APIView):
    def post(self, request):
        otp_code = request.data.get('otp')
        if otp_code == otp:
            return Response({'message': 'Account Verification code is valid'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid OTP code'}, status=status.HTTP_400_BAD_REQUEST)


