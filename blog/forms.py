from django import forms
from .models import Post, PostComment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'image', 'published_date']


class PostCommentForm(forms.ModelForm):

    class Meta:

        model = PostComment
        fields = ['name', 'content']
