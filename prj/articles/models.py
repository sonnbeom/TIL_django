from django.db import models

# Create your models here.
# 파이썬에서 클래스 인자는 상속이다.

'''
0. model 객체를 만든다(스케치본이라 한다.)
1. makemigrations 진행(개발자가 진행) -> 장고가 migration파일을 만든다.
2. migrate를 통해 db에 반영

'''
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add => 처음 생성될 때만 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True)
    # 저장될 때마다 현재 날짜 시간을 저장