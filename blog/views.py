from django.shortcuts import render , get_object_or_404
from . import views
from blog.models import Post,Comment,Myresume
from blog.forms import NewComment , PostCreateForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import CreateView,UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
   
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)

    context = {
        'title' : "الصفحة الرئيسية",
        'posts' : posts,
        'page' : page
    }
    return render(request,'blog/index.html', context) 

def about(request):
    return render(request,'blog/about.html',{"title":"من أنا"})

def resume(request):
    resume= Myresume.objects.all().first()
    return render(request,'blog/resume.html',{"title":"من أنا","resume":resume})    

def details(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    comments = post.comments_of_post.filter(active=True)
    comment_form = NewComment()
    context = {
        'title' : post.title,
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
    }

    if request.method=="POST":
        comment_form=NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            comment_form = NewComment()
   # else:
     #   comment_form = NewComment()

    return render(request,'blog/detail.html',context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ['title','content']
    template_name='blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    model = Post
    #fields = ['title','content']
    template_name='blog/update_post.html'
    form_class = PostCreateForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin, DeleteView):
    model = Post
    success_url="/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

