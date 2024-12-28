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


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'like_count',)

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

    def like_count(self, obj):
        return obj.like.count()

    like_count.short_description = 'Number of post like'
