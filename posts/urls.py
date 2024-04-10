from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = "posts"),
    path('post/<str:pk>', views.post, name = "post"),

    path('create-post/', views.createPost, name = "create-post"),
    path('update-post/<str:pk>', views.updatePost, name = "update-post"),
    path('delete-post/<str:pk>', views.deletePost, name = "delete-post"),

    path('create-category/', views.createCategory, name = "create-category"),

    path('categories/', views.categories, name = "categories"),
    path('category/<str:pk>', views.category, name = "category"),
]