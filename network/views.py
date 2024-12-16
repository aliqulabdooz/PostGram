from django.shortcuts import render, reverse, redirect
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.http import Http404
from django.contrib import messages
from .models import *


def index_view(request):
    if request.user.is_authenticated:
        return redirect(request.user.get_absolute_url())
    context = {
        'redirect_url': reverse('accounts:login_view')
    }
    return render(request, 'accounts/splash.html', context)


@login_required()
def profile_view(request, slug):
    try:
        user = get_object_or_404(CustomUser, slug=slug)
    except Http404:
        return render(request, 'errors/404.html')
    user_post = user.user_posts.all().order_by('-date_created')
    context = {
        'user': user,
        'posts': user_post,
    }
    return render(request, 'network/profile.html', context)


@login_required()
def profile_edit_view(request):
    return render(request, 'network/edit_profile.html')


@login_required()
def allPosts_view(request):
    user_post = request.user.user_posts.all().order_by('-date_created')
    context = {
        'posts': user_post,
    }
    return render(request, 'network/all_post.html', context)


@login_required()
def addPost_view(request):
    redirect_url = ''
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image'] if 'image' in request.FILES else None
        caption = request.POST['caption']
        try:
            post = Post.objects.create(title=title, image_post=image, caption=caption, user_id=request.user.id)
            post.save()
            redirect_url = request.user.get_absolute_url()
        except IntegrityError:
            messages.error(request, 'The title must not be empty.')
            redirect_url = 'network:addPost_view'

        return redirect(redirect_url)

    else:
        return render(request, 'network/add_post.html')