from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=100)
    #content = models.TextField()
    #content = tinymce_models.HTMLField()
    content = RichTextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       # return '/detail/{}'.format(self.pk)
       return reverse('detail',args=[self.pk]) #'تقوم بتوليد الرابط وتوجيه المستخدم اليه'
    
    class Meta():
        ordering = ('-post_date',)


class Comment(models.Model):
    name=models.CharField(max_length=50,verbose_name='الاسم')
    email=models.EmailField(verbose_name='البريد الالكتروني')
    body=models.TextField(verbose_name='التعليق')
    comment_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments_of_post')

    def __str__(self):
        return self.body

    class Meta():
        ordering=('-comment_date' ), 

class Myresume(models.Model):
    lastupdate = models.DateTimeField(auto_now=True)
    resume = RichTextField()

    def __str__(self):
        return "Last update : {}".format(self.lastupdate.strftime('%Y/%m/%d'))