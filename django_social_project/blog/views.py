from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27,2018',
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog post 2',
        'content': '2nd post content',
        'date_posted': 'August 28,2018',
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)

def cutie(request):
    return HttpResponse("<h1>Megan is a cutie.</h1>")
# Create your views here.
