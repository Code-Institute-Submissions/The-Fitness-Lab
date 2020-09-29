from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from .forms import CreatePostForm, PostCommentForm
from django.contrib import messages
from accounts.models import UserAccount
from django.utils import timezone
from datetime import datetime, timedelta
import datetime


def blog(request):
    blog = Post.objects.all()
    context = {
        'blog': blog,
    }

    return render(request, 'blog.html', context)


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        blog = Post.objects.all()
        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = CreatePostForm()

    template = 'create_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def blog_details(request, post_id):

    blog = get_object_or_404(Post, pk=post_id)
    blog.save()
    blog_user = blog.user
    comments = blog.postcomment.all()
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()

    else:
        form = PostCommentForm()
    profile = get_object_or_404(UserAccount, user=request.user)
    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
        'blog_user': blog_user,
        'profile': profile,
    }
    return render(request, 'blog-details.html', context)


@login_required
def edit_comment_blog(request, pk=None):
    """ A view that allows us to add a comment to a post """

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        edit_form = CreatePostForm(request.POST, request.FILES, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,
                             'You have successfully updated your Blog')
            return redirect('blog_details', post.id)

        else:
            messages.error(request, 'Sorry, you are unable to edit this post')
            return redirect('blog')
    else:
        edit_form = CreatePostForm(request.POST, request.FILES, instance=post)
    context = {
        'form': edit_form,
        'post': post,
    }
    return redirect(request, 'edit_blog.html', context)
