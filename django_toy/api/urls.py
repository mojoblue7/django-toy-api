from django.urls import path

from .views import UserInfoListView

app_name = 'api'
urlpatterns = [
    path('user_info/', UserInfoListView.as_view(), name='user_info'),
]