from random import randint

from django.core.exceptions import ValidationError


def check_otp_code(value):
    if len(str(value)) != 6:
        raise ValidationError("OPT code must be 6 digits")


def generate_code():
    code = "".join(str(randint(1, 9)) for _ in range(6))
    return int(code)
