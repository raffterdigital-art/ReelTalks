from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category  # import your models

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        # if your post URL is something like /post/123/ or /post/title-slug/
        return reverse('post_detail', args=[obj.id])  # change if your URL uses slug

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
