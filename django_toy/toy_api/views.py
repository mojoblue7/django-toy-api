from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import UserInfo


def index(request):
    return HttpResponse("민서 바보, world.")

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def users(request):
    users = UserInfo.objects.filter(
        reg_date_at__isnull=False
    ).order_by('-reg_date')
    users_list = serializers.serialize('json', users)
    return HttpResponse(users_list, content_type="text/json-comment-filtered")
