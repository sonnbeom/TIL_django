from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    post_v2 = Post.objects.filter(content_contains = '테스트')
    
    context = {
        'posts' : posts
    }

    return render(request, 'post/index.html', context)