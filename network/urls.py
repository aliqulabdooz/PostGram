from django.urls import path
from . import views

app_name = 'network'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('profile/<slug:slug>', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit_view, name='profile_edit_view'),
    path('allposts/', views.allPosts_view, name='allPosts_view'),
    path('add_post/', views.addPost_view, name='addPost_view'),
]
