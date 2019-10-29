from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all() #=> QuerySet ~= List

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 넘어온 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article.objects.create(title=title, content=content)
    # article.title
    # article.content 

    context = {
        'title': title,
        'content': content,
    }

    return render(request, 'articles/create.html', context)
