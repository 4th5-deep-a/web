from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # /articles/
    path('new/', views.new, name='new'), # /articles/new/
    path('<int:pk>/', views.detail, name='detail'), # /articles/1/, /articles/2/
    path('<int:pk>/edit/', views.edit, name='edit'), # /articles/1/edit/
]