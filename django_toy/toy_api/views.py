from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
# Create your views here.
from .models import UserInfo
from .serializer import UserInfoListSerializer


def index(request):
    return HttpResponse("Hello, world.")


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoListSerializer

# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))
# def users(request):
#     users = UserInfo.objects.filter(
#         reg_date__isnull=False
#     ).order_by('-reg_date')
#     users_list = serializers.serialize('json', users)
#     return HttpResponse(users_list, content_type="text/json-comment-filtered")
