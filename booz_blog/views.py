from django.shortcuts import render

#fake post dictionaries
posts = [
    {
        'author': 'Rustiphyde',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'September 8, 2019'
    },
    {
        'author': 'Razorworm',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 8, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'booz_blog/home.html', context)
def about(request):
    return render(request, 'booz_blog/about.html', {'title': 'About'})

#default Django templates directory structure
#app_name -> templates -> app_name -> templateName.html

