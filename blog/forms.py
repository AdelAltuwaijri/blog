from django import forms
from blog.models import Comment,Post


class NewComment(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name','email','body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label ='عنوان التدوينة',max_length=150)
    content = forms.CharField(label ='المحتوى' , widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title','content']
