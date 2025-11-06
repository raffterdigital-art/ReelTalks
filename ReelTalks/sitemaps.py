from django.contrib.sitemaps import Sitemap
from ReelBlog.models import Post, Category

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        # fallback to simple path if reverse fails
        return f"/blog/{obj.id}/"


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return f"/category/{obj.name}/"  # or obj.slug if your model uses slugs


sitemaps = {
    'posts': PostSitemap,
    'categories': CategorySitemap,
}
