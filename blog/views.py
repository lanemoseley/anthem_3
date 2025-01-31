from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Post
import markdown


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.fenced_code',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    context = {
        "post": post,
    }

    return render(request, "blog_detail.html", context)

