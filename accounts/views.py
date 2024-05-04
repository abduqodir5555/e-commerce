from datetime import timedelta

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response

from accounts.models import *
from accounts.serializers import *
from accounts.utils import *
from core.settings.base import VERIFY_OTP_CODE_TIME


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class VerifyOtpView(APIView):
    serializer_class = VerifyOtpSerializer
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            choice = data.get("choice")
            serializer = VerifyOtpSerializer(data=data)
            if not serializer.is_valid():
                raise APIException(detail="data is not valid")
            user = User.objects.get(email=data.get("email"))
            sms = VerificationOtp.objects.filter(
                user=user,
                type=choice,
                code=data.get('code')
            )
            if not sms.exists():
                data = {
                    "status":False,
                    "message":"OTP code not found"
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if not sms.filter(is_active=True).exists():
                return Response({"message":"otp_code_alredy_actived"})

            if not sms.filter(expires_in__gte=datetime.now()):
                return Response({"message":"time is expired"}, status=status.HTTP_400_BAD_REQUEST)

            sms_obj = sms.last()
            user.is_active=True
            user.save()
            sms_obj.is_active=False
            sms_obj.save()
            return Response({"message": "OTP code actived", "verification":sms_obj.id})

        except User.DoesNotExist:
            raise APIException(detail="User does not exist")

        except Exception as e:
            raise e


class PasswordResetStartView(APIView):
    serializer_class = PasswordResetStartSerializer
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializers = PasswordResetStartSerializer(data=data)
            if not serializers.is_valid():
                return Response(data={"message":"email_is_not_valid"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email=data.get("email"))
            code = generate_code()
            VerificationOtp.objects.create(user=user, type=VerificationOtp.VERIFY_TYPE.RESET_PASSWORD, code=code,
                                           expires_in=datetime.now() + timedelta(minutes=VERIFY_OTP_CODE_TIME))
            send_email(code=code, email=user.email)
            return Response({"message":"send_otp_code_to_email"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            raise APIException(detail={"message":"email not found"})

        except Exception as e:
            raise e


class PasswordResetFinishView(APIView):
    serializer_class = PasswordResetFinishSerializer
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = PasswordResetFinishSerializer(data=data)
            if not serializer.is_valid():
                return Response({"message":"data is not valid", "result":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            sms = VerificationOtp.objects.get(id=data.get("verification"), is_active=False)
            user = sms.user
            user.set_password(data.get("password"))
            user.save()
            return Response({"status":True, "message":"password change successfully"}, status=status.HTTP_200_OK)


        except VerificationOtp.DoesNotExist:
            raise APIException(detail="otp code does not verification")

        except Exception as e:
            raise e













