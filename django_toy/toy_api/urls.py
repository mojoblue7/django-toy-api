from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views
from .views import SignUpView

router = routers.DefaultRouter()
router.register(r'user_info', views.UserInfoViewSet)

app_name = 'toy_api'
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^signup/', SignUpView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^token/', obtain_jwt_token),
    url(r'^token/verify', verify_jwt_token),
    url(r'^token/refresh', refresh_jwt_token),
]
