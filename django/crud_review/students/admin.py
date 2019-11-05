from django.contrib import admin
from .models import Student, Comment


class CommentInline(admin.StackedInline):
    model = Comment

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'created_at', 'updated_at')
    inlines = [
        CommentInline,
    ]

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'content', 'created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)
# admin.site.register(Comment, CommentAdmin)

# 관리자 계정 만들기
# python manage.py createsuperuser