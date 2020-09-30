from django import forms
from .models import Post, PostComment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'published_date']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostCommentForm(forms.ModelForm):

    class Meta:

        model = PostComment
        fields = ['name', 'content']
