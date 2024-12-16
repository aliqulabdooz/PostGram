from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True, blank=True)
    image_profile = models.ImageField(upload_to='accounts/', default='accounts/default-profile.png')
    bio = models.TextField(blank=True)
    USERNAME_REQUIRED = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('network:profile_view', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        if not self.bio:
            self.bio = f"I'm {self.username} and welcome to my profile"
        super().save(*args, **kwargs)
