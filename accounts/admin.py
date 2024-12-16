from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image_profile', 'bio', 'slug')}),
    )
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': (
                 'username', 'email', 'first_name', 'last_name', 'image_profile', 'bio',
                 'password1',
                 'password2',)
         },
         ),
    )
