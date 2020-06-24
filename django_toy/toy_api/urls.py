from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import view_module
from .view_module import AuthView
from .view_module.SignupView import post
from django.urls import path

router = routers.DefaultRouter()

app_name = 'toy_api'
urlpatterns = [
    # path('', view_module.index, name='index'),

    url(r'^signup', post),
    url(r'^', include(router.urls)),
    url(r'^token/', obtain_jwt_token),
    url(r'^token/verify', verify_jwt_token),
    url(r'^token/refresh', refresh_jwt_token),
    path('csrf/', AuthView.csrf),
    # url(r'^login/', ReactView.as_view())
]