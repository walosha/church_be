from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", 'author', 'postId', 'created_at', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['author', "postId", "active", 'body']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", 'author', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['author', "status", 'body']
