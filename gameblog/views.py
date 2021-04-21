from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Post
from django.db.models import Q


# Create your views here.
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Post.CATEGORIES

    context = {'post': post,
               'categories': categories}
    return render(request, 'gameblog/post_details.html', context)


def post_list(request):
    posts_list = Post.objects.all().filter(publish=True)
    title = request.GET.get('title')
    category = request.GET.get('category')
    categories = Post.CATEGORIES
    if title or category:
        posts = Post.objects.all().filter(publish=True).filter(Q(title__icontains=title) |
                                                               Q(category=category))
    paginator = Paginator(posts_list, 2)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'gameblog/post_list.html', context)


def category_list(request, category_id):
    posts = Post.objects.all().filter(publish=True).filter(category=category_id)
    if category_id == 0:
        posts = Post.objects.all().filter(publish=True)

    categories = Post.CATEGORIES
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'gameblog/post_list.html', context)
