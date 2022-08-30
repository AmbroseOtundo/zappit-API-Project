from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    # read null fields
    poster = serializers.ReadOnlyField(source = 'poster.username')
    poster_id = serializers.ReadOnlyField(source = 'poster.id')
    # see how many votes are for a particular post
    votes = serializers.SerializerMethodField()
    # fields to be associated with the API
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created', 'votes']
   
    # function to acknowledge the number of votes
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()
# serializer for voting
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
