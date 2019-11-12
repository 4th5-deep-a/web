from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta: # Class에 대한 정보가 담긴 Class
        model = Article
        fields = ['title', 'content',]


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'title', # class="title"
#                 'placeholder': '제목을 입력하세요.', # placeholder="..."
#             }
#         )
#     )
#     content = forms.CharField(
#         label="내용",
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'content',
#                 'rows': 5,
#                 'cols': 20,
#                 'placeholder': '내용을 입력하세요.',
#             }
#         )
#     )


# Form Class의 용도
# 1. Form Tag 만들기
# 2. Database에 Data 생성하기 위한 틀 제공