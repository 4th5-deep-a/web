from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=40)
    audience = models.IntegerField() # 정수
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField() # 실수
    poster_url = models.TextField()
    description = models.TextField()