from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts')
    image_post = models.ImageField(upload_to='network/', default='default/no-image.png')
    title = models.CharField(max_length=50, blank=False)
    caption = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.image_post:
            self.image_post = 'default/no-image.png'
        if not self.caption:
            self.caption = 'No text is included for the post.'
        super().save(*args, **kwargs)


class Follower(models.Model):
    follow = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_follow')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_following')

    def __str__(self):
        return self.follow.username


class PostLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_likes')
    like = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username


class PostArchive(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_archive')
    archive = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_commented')
    post = models.ManyToManyField(Post)
    comment = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
