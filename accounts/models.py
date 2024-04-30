from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .utils import check_otp_code

from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, verbose_name=_("phone_number"), validators=[RegexValidator(r'^\+?1?\d{9,12}$')], null=True, blank=True)
    address = models.TextField(verbose_name=_("Address"), null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("users")


class VerificationOtp(models.Model):
    class VERIFY_TYPE(models.TextChoices):
        REGISTER = "register", _("Register")
        RESET_PASSWORD = "reset_password", _("Reset password")

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="verification_otp")
    code = models.IntegerField(_("Otp code"), validators=[check_otp_code])
    type = models.CharField(_("Verification Type"), max_length = 30, choices = VERIFY_TYPE.choices)
    expires_in = models.DateTimeField(_("Expires time"))

    def __str__(self):
        return f"{self.user.email} {self.code}"

    class Meta:
        verbose_name = _("Verification otp")
        verbose_name_plural = _("Verification Otps")


class UserAddress(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="user_addresses")
    name = models.CharField(_("Name"), max_length=120)
    phone_number = models.CharField(_("Phone number"), max_length = 120, validators=[RegexValidator(r'^\+?1?\d{9,12}$')])
    apartment = models.CharField(_("Apartment"), max_length=120)
    street = models.TextField(_("Street"))
    pin_code = models.CharField(_("Pin code"), max_length = 120)
    # city = models.ForeignKey()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("User address")
        verbose_name_plural = _("User addresses")