from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from .forms import CreatePost, CommentPostForm

from django.utils import timezone
from datetime import datetime, timedelta
import datetime


def blog(request):
    post = Post.objects.all()
    template = 'blog.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
