from datetime import datetime

from rest_framework import serializers
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import User, VerificationOtp
from .utils import generate_code, send_email


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data.get("email"), is_active=False)
        if user.exists():
            sms = VerificationOtp.objects.get(user=user, type=VerificationOtp.VERIFY_TYPE.REGISTER,
                                             expires_in__gte=datetime.now(), is_active=True)
            if sms:
                sms.expires_in = datetime.now() + settings.OTP_CODE_ACTIVATION_TIME
                code = generate_code()
                sms.code = code
                send_email(code=code, email=user.email)
        else:
            user = super(UserCreateSerializer, self).create(validated_data)
            return user
        return self.create(self, validated_data)



class VerifyOtpSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    email = serializers.CharField(required=True)
    choice = serializers.ChoiceField(choices=VerificationOtp.VERIFY_TYPE)


class PasswordResetStartSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class PasswordResetFinishSerializer(serializers.Serializer):
    verification = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data.get("password") != data.get("password_confirm"):
            raise ValidationError({"status":False, "message":"password is not valid"})
        return data
