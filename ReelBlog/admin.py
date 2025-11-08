from django.contrib import admin
from .models import Category, Post
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'trending', 'image_preview')
    list_filter = ('category', 'trending', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('trending',)
    ordering = ('-created_at',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="50" style="object-fit:cover;border-radius:4px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Preview"

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
