from django.shortcuts import render , redirect
from user.forms import User_Register,LoginForm ,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def user_registration(request):
    if request.method == "POST":
        form = User_Register(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request,f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح')
            return redirect('login')
    else: 
        form = User_Register()
    context = {
        'title' : 'التسجيل',
        'form' : form }

    return render(request,'user/registration.html',context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request,'هناك خطأ في اسم المستخدم أو كلمة المرور')
    
    else:
        form = LoginForm()
    context2 = {
        'title' : 'تسجيل الدخول',
        'form' : form ,}

    return render(request,'user/login.html', context2)

def user_logout(request):
    logout(request)
    return render(request,'user/logout.html',{'title':'تسجيل الخروج',})

@login_required(login_url='login') # Decorator - if user who requested this page is not authenticated, then redirect him to login page
def profile(request):
    posts=Post.objects.filter(author=request.user)
    post_list=Post.objects.filter(author=request.user)
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
   
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request,'user/profile.html',{'title':'الملف الشخصي','posts':posts,'page':page,'post_list':post_list})

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'تم تحديث الملف الشخصي')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)

    context = {
        'title' : 'تعديل الملف الشخصي' ,
        'user_form' : user_form , 
        'profile_form' : profile_form 
        }
    return render(request,'user/profile_update.html', context)