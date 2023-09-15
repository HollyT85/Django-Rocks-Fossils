from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post

def all_posts(request):
    # View all rocks on the rock page
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/posts.html', context)


def post_info(request, post_id):
    # Get individual rock/fossil info
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'posts/post-info.html', context)



# @login_required
# def add_post(request):
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorised to do this.')
#         return redirect(reverse('home'))

    
