from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.published.all()
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, post):
    try:
        post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    except Post.DoesNotExist:
        raise Http404("No Post found")

    return render(request, "post/detail.html", {"post": post})
