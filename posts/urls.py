from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = "posts"),
    path('post/<str:pk>', views.post, name = "post"),

    path('create-post/', views.createPost, name = "create-post"),
    path('update-post/<str:pk>', views.updatePost, name = "update-post"),
    path('delete-post/<str:pk>', views.deletePost, name = "delete-post"),
    path('like-post/<str:pk>/', views.likePost, name='like-post'),
    path('dislike-post/<str:pk>/', views.dislikePost, name='dislike-post'),

    path('create-category/', views.createCategory, name = "create-category"),
    path('update-category/<str:pk>', views.updateCategory, name = "update-category"),
    path('delete-category/<str:pk>', views.deleteCategory, name = "delete-category"),

    path('categories/', views.categories, name = "categories"),
    path('category/<str:pk>', views.category, name = "category"),
]