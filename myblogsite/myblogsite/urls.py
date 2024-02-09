"""
URL configuration for myblogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views  # blog 앱의 views를 임포트

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/blog/', include('blog.urls')),  # blog 앱으로 API 요청을 라우팅
    path('', views.index, name='home'),  # 루트 URL에 대한 뷰 추가
]
