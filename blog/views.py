from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Comment
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

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data["author"]
            comment_body = form.cleaned_data["body"]

            comment = Comment(
                author=comment_author,
                body=comment_body,
                post=post
            )
            comment.save()

            # Send an email alert
            send_mail(
                'ANTHEM_3:  Comment Received',
                str(comment_author) + "\n" + str(comment_body),
                '7496386@gmail.com',
                ['moseley.lane@gmail.com'],
                fail_silently=False,
            )

            return redirect(reverse("blog_index") + str(pk))

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)

