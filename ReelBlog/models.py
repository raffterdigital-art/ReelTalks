from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = CKEditor5Field('Text', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """Return Cloudinary URL even if image missing"""
        if self.image:
            return self.image.url
        return "https://res.cloudinary.com/dhpfmobxq/image/upload/v1720000000/default_placeholder.jpg"
