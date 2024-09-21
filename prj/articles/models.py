from django.db import models

# Create your models here.
# 파이썬에서 클래스 인자는 상속이다.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()