from django.urls import path
from . import views

app_name = 'network'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('explore/', views.explore_view, name='explore_view'),
    path('profile/<slug:slug>', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit_view, name='profile_edit_view'),
    path('allposts/<slug:slug>', views.allPosts_view, name='allPosts_view'),
    path('add_post/', views.addPost_view, name='addPost_view'),
    path('edit_post/', views.edit_post_view, name='edit_post_view'),
    path('delete_post/<int:pk>', views.delete_post_view, name='delete_post_view'),
]