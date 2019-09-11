from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# <app>/<model>_<viewtype>.html