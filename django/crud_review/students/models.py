from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1. DB에 테이블을 생성하기 위한 설계도 생성
    # python manage.py makemigrations

    # 2. 설계도를 가지고 실제 DB에 테이블을 생성
    # python manage.py migrate
