from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # @app.route
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('hi/<str:name>/<int:age>/', views.hi),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('dtl/', views.dtl),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('generate/', views.generate),
    path('article_new/', views.article_new),
    path('article_create/', views.article_create),
    path('static_example/', views.static_example),
]