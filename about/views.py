from django.shortcuts import render
from .models import Post
import markdown


def about_detail(request):
    # If there are multiple "about me" posts, just get the most recent one
    first = Post.objects.all().order_by('-created_on').first()
    if first is not None:
        pk = first.pk
        post = Post.objects.get(pk=pk)
        post.body = markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.fenced_code',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])

    else:
        post = Post()
        post.title = "Whoops! Something went wrong..."

    context = {
        "post": post,
    }

    return render(request, "about_detail.html", context)
