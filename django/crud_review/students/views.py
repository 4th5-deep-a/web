from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    # 1. 모든 student를 DB에서 가져오기
    students = Student.objects.all()

    # 2. context에 저장
    context = {
        'students': students,
    }

    # 3. render하면서 context 넘겨주기
    return render(request, 'students/index.html', context)

def new(request):
    return render(request, 'students/new.html')

# POST 요청을 받는 친구
def create(request):
    # 1. POST 요청으로 넘어온 데이터 가져오기
    name = request.POST.get('name')
    age = request.POST.get('age')

    # 2. Model 클래스 사용해서 DB에 저장!
    student = Student(name=name, age=age)
    student.save()

    # 3. 생성된 학생의 상세 정보를 보는 페이지로 이동(Detail)
    return redirect(f'/students/{student.pk}/')

def detail(request, pk):
    # 1. pk에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk) #=> student 인스턴스

    # 2. context에 저장
    context = {
        'student': student,
    }

    # 3. render하면서 context 넘겨주기
    return render(request, 'students/detail.html', context)


def edit(request, pk):
    # 1. pk에 해당하는 학생 DB에서 가져오기
    student = Student.objects.get(pk=pk)

    # 2. context에 저장
    context = {
        'student': student,
    }

    # 3. render하면서 context 넘겨주기
    return render(request, 'students/edit.html', context)

# POST 요청만을 받음 -> redirect()
def update(request, pk):
    # 1. pk에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk)

    # 2. POST 요청을 통해 넘어온 데이터 가져오기
    name = request.POST.get('name')
    age = request.POST.get('age')

    # 3. student 인스턴스의 정보를 변경 & DB에 반영 -> .save()
    student.name = name
    student.age = age
    student.save()

    # 4. student 상세 페이지로 이동(Detail)
    return redirect(f'/students/{student.pk}')

# POST 요청만을 받음 -> redirect()
def delete(request, pk):
    # 1. pk에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk)

    # 2. student 삭제 (DB에서 삭제하기)
    student.delete()

    # 3. index 페이지로 이동
    return redirect('/students/')