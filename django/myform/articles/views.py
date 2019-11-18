from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     if request.method == 'POST':
#         # 데이터베이스에 데이터 생성 (Form)
#         # 1. 넘어온 데이터를 받기
#         article_form = ArticleForm(request.POST)
#         # title = request.POST.get('title')
#         # content = request.POST.get('content')
#         # 2. 넘어온 데이터 검증
#         if article_form.is_valid():
#             title = article_form.cleaned_data.get('title')
#             content = article_form.cleaned_data.get('content')
#             # 3. 데이터베이스에 Article 만들기!
#             article = Article.objects.create(title=title, content=content)
#             # 4. redirect -> detail
#             return redirect('articles:detail', article.pk)
#     else:
#         article_form = ArticleForm()
#         # 폼을 보여줌
#         context = {
#             'article_form': article_form,
#         }
#         return render(request, 'articles/new.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        # 데이터베이스에 데이터 생성 (ModelForm)
        # 1. 넘어온 데이터를 받기 (title, content)
        article_form = ArticleForm(request.POST)

        # 2. 넘어온 데이터 검증
        if article_form.is_valid():
            # 3. 데이터베이스에 Article 만들기!
            article = article_form.save(commit=False)
            # 3-1. user 정보 끼워넣기
            article.user = request.user
            article.save()

            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()

    # 폼을 보여줌
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)

def detail(request, pk):
    # 1. pk번째 데이터를 가져오기
    article = Article.objects.get(pk=pk)
    # 2. context로 넘겨주기
    context = {
        'article': article,
    }
    # 3. render와 함께 html로 넘겨주기
    return render(request, 'articles/detail.html', context)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.method == 'POST':
#         # Article 수정
#         # 1. 넘어온 데이터 받기
#         article_form = ArticleForm(request.POST)
#         # 2. 데이터 검증
#         if article_form.is_valid():
#             # 3. 검증된 데이터로 수정 & 저장
#             article.title = article_form.cleaned_data.get('title')
#             article.content = article_form.cleaned_data.get('content')
#             article.save()
#             # 4. redirect -> detail
#             return redirect('articles:detail', article.pk)
#     else:
#         # Article 수정하는 Form 보여주기
#         article_form = ArticleForm(
#                 {
#                     'title': article.title,
#                     'content': article.content,
#                 }
#             )
#         context = {
#             'article_form': article_form,
#         }
#         return render(request, 'articles/new.html', context)

@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    # article의 주인인지 검증
    if request.user != article.user:
        return redirect('articles:index')

    if request.method == 'POST':
        # Article 수정
        # 1. 넘어온 데이터 받기
        article_form = ArticleForm(request.POST, instance=article)
        # 2. 데이터 검증
        if article_form.is_valid():
            # 3. 검증된 데이터로 수정 & 저장
            article_form.save()

            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        # Article 수정하는 Form 보여주기
        article_form = ArticleForm(instance=article)

    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)

# POST 요청만 받음
@login_required
def like(request, pk):
    # 1. pk번 article을 가져오기
    article = Article.objects.get(pk=pk)
    # 2. 현재 로그인한 user가 이 article에 좋아요를 눌렀는지?
    if request.user in article.like_users.all():
        # 3-1. 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 3-2. 좋아요
        article.like_users.add(request.user)

    return redirect('articles:detail', pk)