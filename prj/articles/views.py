from django.shortcuts import render, redirect
import random
from .models import Article
from .forms import ArticleForm

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
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'articles/new.html', context)

# def create(request):
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form':form
#     }
#     return render(request, 'articles/new.html', context)

# def edit(request, pk):
#     article = Article.objects.get(pk = pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article':article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     article = Article.objects.get(pk = pk)
#     form = ArticleForm(request.POST, instance=article)

#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES ,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)