from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    # 1. 모든 Movie 가져오기
    movies = Movie.objects.all()

    # 2. context 생성
    context = {
        'movies': movies,
    }

    # 3. context와 함께 render하기
    return render(request, 'movies/index.html', context)

def new(request):
    if request.method == 'POST':
        # DB에 Create
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie.objects.create(
            title=title,
            title_en=title_en,
            audience=audience,
            open_date=open_date,
            genre=genre,
            watch_grade=watch_grade,
            score=score,
            poster_url=poster_url,
            description=description
        )

        return redirect('movies:detail', movie.pk)
        
    else:
        return render(request, 'movies/new.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie.title = title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()

        return redirect('movies:detail', movie.pk)
        
    else:
        context = {
            'movie': movie,
        }
        return render(request, 'movies/edit.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
