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
def explore_view(request):
    posts = Post.objects.all().exclude(user_id=request.user.id)
    context = {
        'posts': posts,
    }
    return render(request, 'network/explore.html', context)


@login_required()
def post_detail_view(request, slug, pk):
    try:
        check_like = False
        check_archive = False
        post = get_object_or_404(Post, user__slug=slug, id=pk)
        user_like = request.user.user_likes.first()
        user_archive = request.user.user_archive.first()
        if user_like:
            check_like = user_like.like.filter(id=post.id).exists()
        if user_archive:
            check_archive = user_archive.archive.filter(id=post.id).exists()
    except Http404:
        return render(request, 'errors/404.html')
    else:
        context = {
            'post': post,
            'check_like': check_like,
            'check_archive': check_archive,
        }
        return render(request, 'network/post_detail.html', context)


@login_required()
def profile_view(request, slug):
    try:
        following_check = None
        following_count = 0
        user = get_object_or_404(CustomUser, slug=slug)
        check_user = user == request.user
        following_parameter = request.user.user_follow.first()
        if not check_user and following_parameter:
            following_check = following_parameter.following.filter(id=user.id).exists()
        if Follower.objects.filter(follow_id=user.id).exists():
            following_count = user.user_follow.first().following.count
    except Http404:
        return render(request, 'errors/404.html')
    user_post = user.user_posts.all().order_by('-date_created')
    context = {
        'user': user,
        'posts': user_post,
        'check_user': check_user,
        'following_check': following_check,
        'following_count': following_count,
    }
    return render(request, 'network/profile.html', context)


@login_required()
def profile_edit_view(request):
    if request.method == "POST":
        user = request.user
        try:
            default_image = request.user.image_profile
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.image_profile = request.FILES['image_profile'] if 'image_profile' in request.FILES else default_image
            user.bio = request.POST['bio']
            if not request.POST['username']:
                messages.error(request, 'username cannot be empty')
            else:
                user.save()
                return redirect(user.get_absolute_url())
        except IntegrityError as e:
            messages.error(request, 'username is already taken')
    return render(request, 'network/edit_profile.html')


@login_required()
def allPosts_view(request, slug):
    try:
        user = get_object_or_404(CustomUser, slug=slug)
        check_user = request.user == user
        user_post = user.user_posts.all().order_by('-date_created')
        user_likes = {}
        user_archives = {}
        if PostLike.objects.filter(user_id=request.user.id).exists():
            post_likes = request.user.user_likes.first().like.all()
            user_likes = set(user_post & post_likes)
        if PostArchive.objects.filter(user_id=request.user.id).exists():
            post_archive = request.user.user_archive.first().archive.all()
            user_archives = set(user_post & post_archive)
    except Http404:
        return render(request, 'errors/404.html')
    context = {
        'posts': user_post,
        'check_user': check_user,
        'user_likes': user_likes,
        'user_archives': user_archives,
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


@login_required()
def edit_post_view(request):
    pk = int(request.GET.get('post'))
    try:
        post = get_object_or_404(Post, id=pk)
        user_posts = request.user.user_posts.all().order_by('-date_created')
        if request.method == "POST":
            print(request.FILES)
            if request.POST['title'] == '':
                messages.error(request, 'title cannot be empty')
                return redirect('network:edit_post_view', pk)
            post.title = request.POST['title']
            post.image_post = request.FILES['image_post'] if 'image_post' in request.FILES else post.image_post
            post.caption = request.POST['caption']
            post.save()
            return redirect(f'{reverse("network:allPosts_view", args=[post.user.slug])}?post={pk}')
        else:
            context = {
                'pk': pk,
                'posts': user_posts,
            }
            return render(request, 'network/all_post.html', context)
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def delete_post_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        if post.user != request.user:
            return redirect(request.user.get_absolute_url())
        post.delete()
        return redirect(request.user.get_absolute_url())
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def follow_view(request, slug):
    try:
        user = get_object_or_404(CustomUser, slug=slug)
        if user == request.user:
            return redirect('network:index_view')
    except Http404:
        return render(request, 'errors/404.html')
    else:
        follow, created = Follower.objects.get_or_create(follow_id=request.user.id)
        if follow.following.filter(id=user.id).exists():
            # I can set a status error
            return redirect('network:index_view')
        follow.following.add(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def unfollow_view(request, slug):
    try:
        redirection = ''
        user = get_object_or_404(CustomUser, slug=slug)
        if Follower.objects.filter(follow_id=request.user.id).exists():
            redirection = request.META.get('HTTP_REFERER', '/')
            follow_check = request.user.user_follow.first().following.remove(user)
        else:
            redirection = 'network:index_view'
        return redirect(redirection)
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def postLike_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        user_like, created = PostLike.objects.get_or_create(user_id=request.user.id)
        if user_like.like.filter(id=post.id).exists():
            return redirect('network:index_view')
        user_like.like.add(post)
        return redirect(f'{reverse("network:allPosts_view", args=[post.user.slug])}?post={pk}')
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def postDislike_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        check_like = request.user.user_likes.first()
        if check_like:
            if check_like.like.filter(id=post.id).exists():
                check_like.like.remove(post)
                return redirect(f'{reverse("network:allPosts_view", args=[post.user.slug])}?post={pk}')
        return redirect('network:index_view')
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def add_comment_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        if 'comment' in request.POST:
            comment = PostComment.objects.create(user=request.user, comment=request.POST['comment'])
            comment.add(post)
            return redirect(request.META.get('HTTP_REFERER', '/'))
        messages.error(request, 'comment cannot be empty!!')
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def postArchive_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        user_archive, created = PostArchive.objects.get_or_create(user_id=request.user.id)
        if user_archive.archive.filter(id=post.id).exists():
            return redirect('network:index_view')
        user_archive.archive.add(post)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def postUnarchive_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        check_archive = request.user.user_archive.first()
        if check_archive:
            if check_archive.archive.filter(id=post.id).exists():
                check_archive.archive.remove(post)
                return redirect(request.META.get('HTTP_REFERER', '/'))
        return redirect('network:index_view')
    except Http404:
        return render(request, 'errors/404.html')


@login_required()
def archive_show_view(request):
    check_user = False
    user_likes = {}
    user_archives = {}
    posts = request.user.user_archive.first().archive.all().order_by('-date_created')
    if PostLike.objects.filter(user_id=request.user.id).exists():
        post_likes = request.user.user_likes.first().like.all()
        user_likes = set(posts & post_likes)
    if PostArchive.objects.filter(user_id=request.user.id).exists():
        post_archive = request.user.user_archive.first().archive.all()
        user_archives = set(posts & post_archive)
    context = {
        'posts': posts,
        'check_user': check_user,
        'user_likes': user_likes,
        'user_archives': user_archives,
    }
    return render(request, 'network/all_post.html', context)
