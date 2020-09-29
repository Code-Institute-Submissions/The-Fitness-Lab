from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:post_id>/', views.blog_details, name='blog_details'),
    path('edit/<int:pk>/',
         views.edit_blog_post, name='edit_blog_post'),
]
