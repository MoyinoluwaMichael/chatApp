import os
from smtplib import SMTPConnectError

from django.core.mail import send_mail

from chat_app_project.settings import BASE_DIR

file_path = os.path.join(BASE_DIR, '', 'secret.txt')

with open(file_path, 'r') as file:
    credentials = file.readlines()

SYSTEM_EMAIL_ADDRESS = credentials[0].strip()


def sendOnboardingMail(username: str, otp: str, email) -> None:
    subject = 'Registration Confirmation'
    message = 'Hello {},\n\nThank you for registering. Your account has been created.' \
              ' Use this OTP {} to verify your account.'.format(username, otp)
    from_email = SYSTEM_EMAIL_ADDRESS
    recipient_list = [email]
    try:
        send_mail(subject, message, from_email, recipient_list)
    except SMTPConnectError:
        print("Service unavailable. Unable to send mail.")
