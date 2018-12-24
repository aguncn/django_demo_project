from django.contrib import admin
from bbs.models import Board, Topic, Post
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'caption', 'author', 'publish_time')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'caption', 'author', 'publish_time')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'caption', 'author', 'publish_time')

