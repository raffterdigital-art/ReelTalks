from django.contrib import admin
from .models import Post, Category
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'trending', 'image_tag')
    list_filter = ('category', 'trending')
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
