from django.contrib.auth import get_user_model
from django import forms
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
User = get_user_model()

class Registerform(forms.Form):
    username = forms.CharField(max_length=20 , min_length=2 , error_messages={
        'required' : '用户名不能为空',
        'min_length' : '用户名长度国小,请重新输入',
        'max_length' : '用户名长度过长,请重新输入',
    })
    email = forms.EmailField( error_messages={
        'required' : '邮箱不能为空',
        'invalid' : '请传入一个正确的邮箱'
    })
    ma = forms.CharField(max_length=4 , min_length=4,error_messages={
        'required' : '验证码不能为空'
    })
    password = forms.CharField(max_length=20 , min_length=6 , error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度国小,请重新输入',
        'max_length': '密码长度过长,请重新输入',
    })
    def clean_email(self):
        email = self.cleaned_data.get('email')
        f = User.objects.filter(email=email).exists()
        if f == True :
            raise forms.ValidationError('邮箱已经被注册')
        else :
            return email
    def clean_ma(self):
        ma = self.cleaned_data.get('ma')
        email = self.cleaned_data.get('email')
        result = yanzheng.objects.filter(email=email , ma=ma).first()
        if not result :
            raise forms.ValidationError("邮箱未注册或验证码不匹配")
        result.delete()
        return ma

class Loginform(forms.Form):
    email = forms.EmailField(error_messages={
        'required': '邮箱不能为空',
        'invalid': '请传入一个正确的邮箱'
    })
    password = forms.CharField(max_length=20 , min_length=6 , error_messages={

    })
    remember = forms.IntegerField(required=False)

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']