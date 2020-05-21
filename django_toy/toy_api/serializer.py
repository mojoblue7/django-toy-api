from rest_framework import serializers

from .models import UserInfo


# UserInfo 리스트 시리얼라이저, api에서 보여줄 필드 명시
class UserInfoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'email', 'username', 'gender', 'reg_date', 'mod_date')
