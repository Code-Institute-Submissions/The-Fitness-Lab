from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from .forms import CreatePostForm, CommentPostForm

from django.utils import timezone
from datetime import datetime, timedelta
import datetime


def blog(request):
    post = Post.objects.filter(published_date__lte=timezone.now()
                               ).order_by('-published_date')
    template = 'blog.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        post = Post.objects.all()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(reverse('blog'))
    else:
        form = CreatePostForm()

    template = 'create_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
