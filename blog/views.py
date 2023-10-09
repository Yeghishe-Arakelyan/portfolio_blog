from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostCategory


def paginat(request, list_objects, per_page=20):  
    p = Paginator(list_objects, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj

def blog_home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': paginat(request, posts)}
    return render(request, 'post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    category = post.category.first()
    if category:
        related_posts = Post.objects.filter(category=category).exclude(slug=slug)[:5]
    else:
        related_posts = []
    
    context = {
        'title': post.title,
        'post': post,
        'related_posts': related_posts
    }
    return render(request, 'post_detail.html', context)


