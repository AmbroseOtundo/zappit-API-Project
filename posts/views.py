from xmlrpc.client import ResponseError
from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from posts import serializers
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# class based view to list out info
# we are a pulling a db using the qeueryset
# type of serializer to use

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# permission to create this api
    permission_classes = [IsAuthenticatedOrReadOnly]


# create a field without choosing the current api user.
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

# UPVOTE VIEW... the mixins.DestroyModelMixin deletes votes
class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        # check if use has voted or check a particular post user is already is existence
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post:) ')

        serializer.save(voter=self.request.user, post = Post.objects.get(pk=self.kwargs['pk']))

# delete functionality, we use mixins-- this deletes a vote.
    def delete(self, request, *args, **kwargs):
        # 1. IF A VOTE EXISTS
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post')


# delete a post
class PostRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# permission to create this api
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'],  poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This is not your post to delete')

