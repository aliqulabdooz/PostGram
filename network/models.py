from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts')
    image_post = models.ImageField(upload_to='network/', default='network/no-image.png')
    title = models.CharField(max_length=50, blank=False)
    caption = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.image_post:
            self.image_post = 'network/no-image.png'
        if not self.caption:
            self.caption = 'No text is included for the post.'
        super().save(*args, **kwargs)
