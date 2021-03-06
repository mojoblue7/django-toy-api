from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user_info', views.UserInfoViewSet)

app_name = 'toy_api'
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
