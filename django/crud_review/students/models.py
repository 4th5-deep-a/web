from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill, ResizeToFit
# Thumbnail(가로, 세로) - 썸네일
# ResizeToFill(300, 300) - 원본 비율 유지, 해상도를 넘어가는 부분 잘라냄
# ResizeToFit(300, 300) - 원본 비율 무시, 대신 모든 이미지가 보이도록 압축

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    image = ProcessedImageField(
        blank=True,
        upload_to='students/images', # 업로드 위치
        processors=[ResizeToFill(300, 300)], # 처리할 작업들 목록
        format='jpeg', # 저장 포멧 - jpg, png 등 사용 가능
        options={
            'quality': 90, # 옵션
        },
    )
    # image = models.ImageField(blank=True)
    # blank=True -> 비어 있는 값(ex. '')이 들어올 수 있음.
    # null=True -> None(NULL)이 들어올 수 있음.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1. DB에 테이블을 생성하기 위한 설계도 생성
    # python manage.py makemigrations

    # 2. 설계도를 가지고 실제 DB에 테이블을 생성
    # python manage.py migrate

# Student : Comment = 1 : N
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # CASCADE - 1:N에서 1이 삭제되면 N도 삭제
    # PROTECT - 1을 삭제하려 할 때, N이 있으면 삭제 불가능
    # SET_NULL - 1이 삭제가 되면, N의 컬럼에 NULL로 설정
    # DO_NOTHING - 아무것도 하지 않음

    # 1. 1번 학생(1) 가져오기
    # student = Student.objects.get(pk=1)

    # 2. 댓글(N) 생성
    # comment = Comment()
    # comment.content = 'First Comment'
    # comment.student = student
    # (comment.student_id = student.pk)
    # comment.save()

    # 3. 댓글(N)로부터 학생(1) 불러오기
    # comment.student #=> student 인스턴스 자체
    # comment.student.name #=> 학생 이름
    # comment.student.age #=> 학생 나이

    # 4. 학생(1)으로부터 댓글(N) 불러오기
    # student.comment_set.all() #=> comment QuerySet
