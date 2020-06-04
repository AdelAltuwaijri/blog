from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class User_Register(forms.ModelForm):
    username=forms.CharField(label="اسم المستخدم",max_length=20)
    email=forms.CharField(label="البريد الالكتروني")
    first_name=forms.CharField(label="الاسم الأول")
    last_name=forms.CharField(label="الاسم الاخير")
    password1=forms.CharField(label="كلمة المرور",widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label="تأكيد كلمة المرور",widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
    
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username = cd['username']).exists():
            raise forms.ValidationError ('هذا الاسم مسجل مسبقا ، فضلا قم ياختيار اسم آخر')
        return cd['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور ' , widget=forms.PasswordInput() )
    class Meta:
    
        model = User
        fields = ('username','password')

class UserUpdateForm(forms.ModelForm):
    email=forms.CharField(label="البريد الالكتروني")
    first_name=forms.CharField(label="الاسم الأول")
    last_name=forms.CharField(label="الاسم الاخير")
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
