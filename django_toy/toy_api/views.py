from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import rest_framework.generics, rest_framework.serializers
from rest_framework.response import Response
from .models import UserInfo


def index(request):
    return HttpResponse("민서 바보, world.")


# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))
def users(request):
    users = UserInfo.objects.filter(
        reg_date__isnull=False
    ).order_by('-reg_date')
    users_list = serializers.serialize('json', users)
    return HttpResponse(users_list, content_type="text/json-comment-filtered")


# UserInfo 리스트 시리얼라이저, api에서 보여줄 필드 명시
class UserInfoListSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'email', 'username', 'gender', 'reg_date', 'mod_date')


# api/userinfo로 get 하면 listView로 연결
class UserInfoListView(rest_framework.generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializers = UserInfoListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(rest_framework.serializer.data)

        return Response(rest_framework.serializer.data)
