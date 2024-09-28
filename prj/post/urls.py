from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('index/', views.index, name = 'index'),
]