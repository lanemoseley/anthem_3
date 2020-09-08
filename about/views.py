from django.shortcuts import render
from .models import Post


def about_detail(request):
    first = Post.objects.all().order_by('-created_on').first()
    if first is not None:
        pk = first.pk
        post = Post.objects.get(pk=pk)
    else:
        post = Post()
        post.title = "Whoops! Something went wrong..."

    context = {
        "post": post,
    }

    return render(request, "about_detail.html", context)
