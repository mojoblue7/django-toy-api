"""django_toy URL Configuration

The `urlpatterns` list routes URLs to view_module. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function view_module
    1. Add an import:  from my_app import view_module
    2. Add a URL to urlpatterns:  path('', view_module.home, name='home')
Class-based view_module
    1. Add an import:  from other_app.view_module import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'django_toy'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('toy_api/', include('toy_api.urls')),
    path('api/', include('api.urls')),
    # path('api/token/', obtain_jwt_token),           # JWT 토큰을 발행
    # path('api/token/verify/', verify_jwt_token),    # JWT 토큰 유효성 검증
    # path('api/token/refresh/', refresh_jwt_token),  # JWT 토큰 갱신
]
