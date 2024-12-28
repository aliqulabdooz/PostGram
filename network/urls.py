from django.urls import path
from . import views

app_name = 'network'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('explore/', views.explore_view, name='explore_view'),
    path('profile/<slug:slug>', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit_view, name='profile_edit_view'),
    path('allposts/<slug:slug>', views.allPosts_view, name='allPosts_view'),
    path('post_detail/<slug:slug>/<int:pk>', views.post_detail_view, name='post_detail_view'),
    path('add_post/', views.addPost_view, name='addPost_view'),
    path('edit_post/', views.edit_post_view, name='edit_post_view'),
    path('delete_post/<int:pk>', views.delete_post_view, name='delete_post_view'),
    path('follow/<slug:slug>', views.follow_view, name='follow_view'),
    path('unfollow/<slug:slug>', views.unfollow_view, name='unfollow_view'),
    path('like/<int:pk>', views.postLike_view, name='postLike_view'),
    path('dislike/<int:pk>', views.postDislike_view, name='postDislike_view'),
    path('add_comment/<int:pk>', views.add_comment_view, name='add_comment_view'),
    path('archive/<int:pk>', views.postArchive_view, name='postArchive_view'),
    path('unarchive/<int:pk>', views.postUnarchive_view, name='postUnarchive_view'),
    path('archive_show/', views.archive_show_view, name='archive_show_view'),
]
