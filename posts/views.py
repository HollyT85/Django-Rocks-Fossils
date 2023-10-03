from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def all_posts(request):
    # View all posts on the blog page
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/posts.html', context)


def post_info(request, post_id):
    # Get individual post info
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'posts/post-info.html', context)



@login_required
def add_post(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            return redirect(reverse('post_info', args=[post.id]))

    else:
        post_form = PostForm()

    template = 'posts/add_post.html'
    context = {
        'post_form': post_form,
    }

    return render(request, template, context)


@login_required()
def edit_post(request, post_id):

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse('post_info', args=[post.id]))
        else:
            console.log('failed')
    else:
        post_form = PostForm(instance=post)

    template = 'posts/edit_post.html'
    context = {
        'post_form': post_form,
        'post': post
    }

    return render(request, template, context)
