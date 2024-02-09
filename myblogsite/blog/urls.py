from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 라우터를 생성하고 뷰셋을 등록합니다.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'categories', views.CategoryViewSet)

# API URL은 이제 라우터에 의해 자동으로 결정됩니다.
urlpatterns = [
    path('', include(router.urls)),
]
