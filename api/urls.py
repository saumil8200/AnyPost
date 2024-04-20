from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('posts/', views.getPosts),
    path('post/<str:pk>', views.getPost),
    path('post/<str:pk>/like/', views.postLike),
    path('post/<str:pk>/dislike/', views.postDislike),
]