from . import views
from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, LikeView


urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>', LikeView, name='like_post')
]