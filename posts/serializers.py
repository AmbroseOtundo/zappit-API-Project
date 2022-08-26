from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # fields to be associated with the API
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'created']
   

