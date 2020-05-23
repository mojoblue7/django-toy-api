
import bcrypt as bcrypt
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.views import View

from .models import UserInfo
from .serializer import UserInfoListSerializer


def index(request):
    return HttpResponse("Hello, world.")


# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoListSerializer

class SignUpView(View):

    def get(self,request):
        print(request.method)
        return render(request, 'toy_api/signup.html')

    def post(self, request):
        data = request.POST

        try:
            if UserInfo.objects.filter(email=data['email']).exists():
                print('망함')
                return JsonResponse({"message" : "EMAIL_EXISTED"}, status=400)

            #   비밀번호 암호화
            password = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_crypt = password_crypt.decode('utf-8')

            #  계정 회원가입
            UserInfo(
                email = data['email'],
                password = password_crypt,
                username = data['username']
            ).save()
            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"})
# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))
# def users(request):
#     users = UserInfo.objects.filter(
#         reg_date__isnull=False
#     ).order_by('-reg_date')
#     users_list = serializers.serialize('json', users)
#     return HttpResponse(users_list, content_type="text/json-comment-filtered")
