from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea())

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
         label='제목',
         widget=forms.TextInput(
              attrs={
                   'class': 'my-title',
                   'place-holder': '제목을 입력해주세요',
                   'maxLength':10,
              }
         )
    )
    class Meta:
         model = Article
         fields = '__all__'
        #  exclude = ('title',)

class ArticleForm_v2(forms.ModelForm):
     class Meta:
          model = Article
          fields = '__all__'
