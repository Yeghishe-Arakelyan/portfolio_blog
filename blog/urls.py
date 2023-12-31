from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home_page, name='blog_home_page'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
