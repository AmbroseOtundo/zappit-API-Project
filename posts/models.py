from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# how the post will look like
class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # order of creation
    class Meta:
        ordering = ['-created']

# prevent one from voting more than one time 

class Vote(models.Model):
    voter =  models.ForeignKey(User, on_delete=models.CASCADE)
    # specific vote being voted
    post = models.ForeignKey(Post, on_delete=models.CASCADE)