from datetime import datetime , timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, VerificationOtp
from .tasks import send_otp_code_to_email
from .utils import generate_code
from core.settings.base import VERIFY_OTP_CODE_TIME


@receiver(post_save, sender=User)
def create_verification_otp(sender, instance, created, **kwargs):
    if created:
        code = generate_code()
        VerificationOtp.objects.create(user=instance, type=VerificationOtp.VERIFY_TYPE.REGISTER, code=code,
                                       expires_in=datetime.now()+timedelta(minutes=VERIFY_OTP_CODE_TIME))
        send_otp_code_to_email(code=code, email=instance.email)