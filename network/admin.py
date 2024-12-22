from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'title', 'date_created')
    list_filter = ('date_created', 'date_modified')
    search_fields = ('title', 'user__username')


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('follow__username',)
