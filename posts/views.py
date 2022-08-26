from django.shortcuts import render
from posts import serializers
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
# class based view to list out info
# we are a pulling a db using the qeuerset
# type of serializer to use

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer