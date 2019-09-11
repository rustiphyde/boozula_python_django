from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
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
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'main_alcohol', 'ingredients', 'preparation']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'title', 'main_alcohol', 'ingredients', 'preparation']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
def about(request):
    return render(request, 'booz_blog/about.html', {'title': 'About'})