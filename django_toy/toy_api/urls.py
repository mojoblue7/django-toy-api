from django.urls import path

from . import views
from .views import UserInfoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('user_info/', UserInfoListView.as_view(), name='user_info'),

]