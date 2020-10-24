from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from api.v1.apps.users.models import EmailOTP
from rest_framework.response import Response
import random
from .models import User
from .serializers import CreateUserSerializer, UserSerializer
from django.contrib.auth.hashers import make_password

def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)

# Create your views here.
def send_conf_email(email):
    otp = random.randint(1, 9999)
    EmailOTP.objects.create(email=email, otp_code=otp)
    send_mail('Activation code', f'This is your activation code: {otp}', email, [f'{email}'])


class SendConfirmOtpToEmail(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data['email']
        if not User.objects.filter(email=email):
            send_conf_email(email)
            return Response({'status': True, 'mes': 'Email OTP SEND!'})
        else:
            return Response({'status': True, 'mes': 'Этот email уже занят'})


class ConfirmEmailOTP(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        otp = request.data['otp']
        email = request.data['email']
        otp_model = EmailOTP.objects.filter(email=email)
        if otp_model:
            otp_model = EmailOTP.objects.get(email=email)
            print(otp_model.otp_code, otp)
            if otp_model.otp_code == int(otp):
                otp_model.is_activated = True
                otp_model.save()
                print('1')
                return Response({'status': True, 'mes': 'Email confim'})
            else:
                print('2')
                return Response({'status': False, 'mes': 'ERROR'})
        else:
            return Response({'status': False, 'mes': 'ERROR'})


class UserView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request):
        if request.user:
            return Response(UserSerializer(request.user).data)
        return super(UserView, self).retrieve(request)


class RegisteringNewUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        if name and email and password:
            if EmailOTP.objects.filter(email=email):
                otp_email = EmailOTP.objects.get(email=email)
                if otp_email.is_activated:
                    temp_data = {
                        'name': name,
                        'email': email,
                        'password': make_password(password)
                    }
                    serializer = CreateUserSerializer(data=temp_data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    otp_email.delete()
                    return Response({
                        'status': True,
                        'detail': 'Пользователь создан!',
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': "Смс код не подтвержден!"
                    })
            else:
                return Response({
                    'status': False,
                    'detail': "Сначала подтвердите email "
                })
        else:
            return Response({
                'status': False,
                'detail': "В запросе должен быть email, пароль, имя"
            })
