from django.core.mail import send_mail


def sendOnboardingMail(username: str, otp: str, email) -> None:
    subject = 'Registration Confirmation'
    message = 'Hello {},\n\nThank you for registering. Your account has been created.' \
              ' Use this OTP {} to verify your account.'.format(username, otp)
    from_email = '7ate9CHAT@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
