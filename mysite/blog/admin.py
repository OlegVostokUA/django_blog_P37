from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'author')
    search_fields = ('title', 'body')
    ordering = ['status', '-publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'post')
    search_fields = ('name', 'body', 'email')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
