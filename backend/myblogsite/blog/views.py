from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

def index(request):
    return render(request, 'blog/index.html')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
