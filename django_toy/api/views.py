from rest_framework import generics, viewsets
from rest_framework.response import Response

# Create your views here.

from toy_api.models import UserInfo

# api/userinfo로 get 하면 listView로 연결
from toy_api.serializer import UserInfoListSerializer


class UserInfoListView(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializers = UserInfoListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)
