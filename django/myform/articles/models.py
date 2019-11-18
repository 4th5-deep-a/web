from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1:N (User:Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Article을 작성한 User -> article.user
    # User가 작성한 모든 Article -> user.article_set.all()
    # M:N [Like] - User:Article
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # Article에 좋아요 누른 모든 User -> article.like_users.all()
    # User가 좋아요 누른 모든 Article -> user.article_set.all() -> user.like_articles.all()


# Auth
# 1. Authetication (인증)
# 2. Authorization (권한)