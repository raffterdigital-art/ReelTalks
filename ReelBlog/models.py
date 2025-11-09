from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


def cloudinary_upload_path(instance, filename):
    """Custom path — keeps title-based name and foldered uploads"""
    safe_title = slugify(instance.title)
    return f"reeltalks_uploads/{safe_title}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = CloudinaryField(
        'image',
        folder='reeltalks_uploads',
        use_filename=True,
        unique_filename=False,
        overwrite=True,
        blank=True,
        null=True,
        public_id=cloudinary_upload_path
    )
    content = CKEditor5Field('Text', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """Return Cloudinary URL or default placeholder"""
        if self.image:
            return self.image.url
        return "https://res.cloudinary.com/dhpfmobxq/image/upload/v1720000000/default_placeholder.jpg"
