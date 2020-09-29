from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from .forms import CreatePostForm, PostCommentForm, EditPostForm  # add before deployment
from accounts.models import UserAccount


def blog(request):
    """
    A view that allows us to view all the blog post
    """

    blog = Post.objects.all()
    context = {
        'blog': blog,
    }

    return render(request, 'blog.html', context)


@login_required
def create_blog(request):
    """
    A view that allows us to create a blog post
    """

      profile = get_object_or_404(UserAccount, user=request.user)
       if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES)
            blog = Post.objects.all()
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                return render(request, 'blog.html', {'blog': blog})

        else:
            form = CreatePostForm()

        template = 'create_blog.html'
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, template, context)


@login_required
def blog_details(request, post_id):
    """ 
    A view that allows us to view a specific blog post 
    """

    edit = CreatePostForm(request.POST, request.FILES)
    blog = get_object_or_404(Post, pk=post_id)
    blog.save()
    blog_user = blog.creator
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
        'edit': edit,
        'blog': blog,
        'comments': comments,
        'form': form,
        'blog_user': blog_user,
        'profile': profile,
    }
    return render(request, 'blog-details.html', context)


@login_required
def edit_blog_post(request, pk):
    """ 
    A view that allows us to edit a blog post 
    """

    blog = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        blog = get_object_or_404(Post, id=pk)
        edit_form = CreatePostForm(request.POST, request.FILES, instance=blog)
        if edit_form.is_valid():
            instance = edit_form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('blog_details', blog.id)

        else:
            return redirect('blog')
    else:
        edit_form = CreatePostForm(request.POST, request.FILES, instance=blog)

    template = 'edit_blog.html'
    context = {
        'form': edit_form,
        'blog': blog,
    }
    return render(request, template, context)
