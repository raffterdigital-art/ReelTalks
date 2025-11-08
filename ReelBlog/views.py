from django.shortcuts import render, get_object_or_404
from .models import Post, Category

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    posts = Post.objects.order_by('-created_at')
    featured = posts.first()
    recent_posts = posts[1:11]
    trending_posts = Post.objects.filter(trending=True).order_by('-created_at')[:10]
    categories = Category.objects.all()
    return render(request, 'ReelBlog/Home.html', {
        'featured': featured,
        'recent_posts': recent_posts,
        'categories': categories,
        'trending_posts': trending_posts,
    })


def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    categories = Category.objects.all()

    # Get other posts in the same category (excluding current post)
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)[:6]

    context = {
        'post': post,
        'categories': categories,
        'related_posts': related_posts,
    }
    return render(request, 'ReelBlog/blog_detail.html', context)

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'ReelBlog/category_posts.html', {'category': category, 'posts': posts, 'categories': categories})

def about(request):
    categories = Category.objects.all()
    return render(request, 'ReelBlog/about.html', {'categories': categories})

def contact(request):
    categories = Category.objects.all()
    return render(request, 'ReelBlog/contact.html', {'categories': categories})

def privacy_policy(request):
    categories = Category.objects.all()
    return render(request, 'ReelBlog/privacy_policy.html', {'categories': categories})