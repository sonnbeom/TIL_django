from django.shortcuts import render

# Create your views here.
def index_article(request):
    context = {
        'name': 'soony',
    }
    return render(request, 'articles/index_past.html', context)