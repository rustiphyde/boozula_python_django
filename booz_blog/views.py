from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'booz_blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name='booz_blog/home.html'
    # set variable from object_list to posts
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['image', 'title', 'main_alcohol', 'ingredients', 'preparation']
    
def about(request):
    return render(request, 'booz_blog/about.html', {'title': 'About'})