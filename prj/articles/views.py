from django.shortcuts import render
import random
from .models import Article
# Create your views here.
def index_article(request):
    context = {
        'name': 'soony',
    }
    return render(request, 'articles/index_past.html', context)

def dinner(request):
    foods = ['국밥', '고기', '라면', '감자']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)

def index(request):
    articles = Article.objects.all()
    articles_v2 = Article.objects.filter(content__contains='!')
    print(articles_v2)
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)