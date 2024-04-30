from random import randint

from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from core.settings.base import EMAIL_HOST

def check_otp_code(value):
    if len(str(value)) != 6:
        raise ValidationError("OPT code must be 6 digits")


def send_email(code, email):
    message = f"Your OTP code is {code}"
    send_mail(subject = "Registration otp code", message=message, from_email = EMAIL_HOST, recipient_list = [email],
              fail_silently=True)


def generate_code():
    code = "".join(str(randint(1, 9)) for _ in range(6))
    return int(code)
