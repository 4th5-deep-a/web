from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id') #=> QuerySet ~= List

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request): # POST 요청을 받음
    # 넘어온 데이터 받기
    # 이유 2번 - GET(URL), POST(http body)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.create(title=title, content=content)
    # article.title
    # article.content 

    return redirect(f'/articles/{article.pk}/')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. pk에 해당하는 article 가져오기
    article = Article.objects.get(pk=pk)

    # 2. edit로부터 넘어온 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 3. 넘어온 데이터를 article에 새롭게 저장
    article.title = title
    article.content = content
    article.save()

    return redirect(f'/articles/{article.pk}/') # detail 페이지