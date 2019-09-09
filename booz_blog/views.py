from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'booz_blog/home.html', context)

def about(request):
    return render(request, 'booz_blog/about.html', {'title': 'About'})

#default Django templates directory structure
#app_name -> templates -> app_name -> templateName.html

