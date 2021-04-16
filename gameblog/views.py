from django.shortcuts import render
from .models import Post
from django.db.models import Q


# Create your views here.
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'gameblog/post_details.html', context)


def post_list(request):
    posts = Post.objects.all().filter(publish=True)
    context = {
        'posts': posts
    }
    return render(request, 'gameblog/post_list.html', context)

