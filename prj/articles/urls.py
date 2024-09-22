from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index_article),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.greeting),
]