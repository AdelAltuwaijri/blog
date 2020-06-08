from django import forms
from blog.models import Comment,Post
#from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
class NewComment(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name','email','body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label ='عنوان التدوينة',max_length=150)
    content = forms.CharField(label ='المحتوى' , widget=CKEditorWidget)
    
   # content = forms.CharField(label ='المحتوى' , widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ['title','content']
