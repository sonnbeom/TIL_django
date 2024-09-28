from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index_past/', views.index_article),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.greeting),
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # path('edit/<int:pk>/', views.edit, name = 'edit'),
    path('update/<int:pk>/', views.update, name='update'),
]