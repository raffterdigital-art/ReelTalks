from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columns visible in Django admin list page
    list_display = ('title', 'category', 'created_at', 'trending', 'image_preview')
    list_filter = ('category', 'trending', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('trending',)
    ordering = ('-created_at',)

    # ✅ Thumbnail image preview (safe even for Cloudinary)
    def image_preview(self, obj):
        if obj.image:
            try:
                return format_html(
                    '<img src="{}" width="100" height="60" '
                    'style="object-fit:cover;border-radius:6px;border:1px solid #ddd;" />',
                    obj.image.url
                )
            except Exception:
                return "Image not available"
        return "No Image"

    image_preview.short_description = "Preview"

    # ✅ Admin actions for bulk updating
    actions = ["make_trending", "remove_trending"]

    def make_trending(self, request, queryset):
        updated = queryset.update(trending=True)
        self.message_user(request, f"{updated} post(s) marked as trending 🔥")

    def remove_trending(self, request, queryset):
        updated = queryset.update(trending=False)
        self.message_user(request, f"{updated} post(s) removed from trending ❌")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
