from django.urls import include, path

from . import views
from .views import (
    PostDetailView, PostListView, PostCreateView,
    PostUpdateView, PostDeleteView, UserPostListView,
)

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view() , name='user-post'),
    path('post/<int:pk>', PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view() , name='post-delete'), # template : <model>_confirm_delete.html
    path('post/<int:pk>/update', PostUpdateView.as_view() , name='post-update'), # template : <model>_form.html
    path('post/new', PostCreateView.as_view() , name='post-create'), # template : <model>_form.html
    path('about/', views.about, name='blog-about'),
]
