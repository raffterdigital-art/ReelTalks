from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from yourapp.models import Post  # change to your model name

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # if your model has an updated_at field

sitemaps = {
    'posts': PostSitemap,
}
