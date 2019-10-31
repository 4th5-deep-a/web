from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/delete/', views.delete),
]