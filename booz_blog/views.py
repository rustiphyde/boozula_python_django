from django.shortcuts import render, redirect
from .models import Post
from .forms import PicUpdateForm
from django.contrib import messages
from django.views.generic import ListView

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
    
def about(request):
    return render(request, 'booz_blog/about.html', {'title': 'About'})

def poster(request):
    if request.method == 'POST':
        pic_form = PicUpdateForm(request.POST, 
                                 request.FILES, 
                                 instance=request.post)
        if pic_form.is_valid():
            pic_form.save()
            messages.success(request, f'Your post has been updated!')
            return redirect('blog-home')
            
    else:
        pic_form = PicUpdateForm(instance=request.post)
    
    context = {
        'pic_form': pic_form
    }
    return render(request, 'booz_blog/home.html', context)


