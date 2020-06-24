import bcrypt as bcrypt
import jwt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
# Create your view_module here.
from rest_framework.utils import json
from rest_framework.views import APIView
from django.views import View

from django_toy.toy_api.forms import SignUpForm
from django_toy.toy_api.models import UserInfo
from django_toy.toy_api.serializer import UserInfoListSerializer
from django_toy.toy_api.utils.loader import secret_key_loader


def index(request):
    return HttpResponse("Hello, world.")


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoListSerializer



class TokenCheckView(View):
    def post(self, request):
        data = json.loads(request.body)

        user_token_info = jwt.decode(data['token'], secret_key_loader(), algorithm='HS256')

        if UserInfo.objects.filter(email=user_token_info['email']).exists():
            return HttpResponse(status=200)

        return HttpResponse(status=403)

