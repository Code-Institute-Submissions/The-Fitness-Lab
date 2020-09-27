from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    """
    Model for the Blog Post
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):

    post = models.ForeignKey(
        Post, related_name='postcomment', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
