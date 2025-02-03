import random
import string
from django.contrib import messages
from .models import *
from django.shortcuts import render,redirect,reverse
from django.http.response import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import  require_http_methods
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
@require_http_methods(['GET', 'POST'])
def login1(request):
    if request.method == 'GET':
        return render(request , 'login.html')
    else :
        form = Loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                if not remember :
                    # 设置过期时间
                    request.session.set_expiry(0)
                return redirect('/')
            else :
                form.add_error(None, '账号或密码错误')
                # print(reverse('author:login'))
                return render(request , 'login.html' , context = {'form':form})
        else :
            form.add_error(None , "账号或密码错误")
            return render(request , 'login.html' , context = {'form':form})
@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request , 'register.html')
    else:
        form = Registerform(request.POST)
        # 已经做完校验了
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(reverse('author:login'))
        else :
            # print(form.errors , 22222222)

            return redirect(reverse('author:register'))

def send_yanzheng(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code' : 400 , 'message' : '必须传递正确的邮箱'})
    else:
        s = "".join(random.sample(string.digits , 4))

        try :
            send_mail(
                'HUY1博客验证码' ,
                message=f"您的注册验证码为{s}",
                recipient_list=[email],
                from_email=None
            )
            yanzheng.objects.update_or_create(email=email, defaults={'ma': s})
            return JsonResponse({'code' : 200 , 'message' : '成功'})
        except Exception as e:
            return JsonResponse({'code' : 500 , 'message' : '邮箱发送失败,请验证您邮箱的正确性'})

def out(request):
    logout(request)
    return redirect('/')

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        print('POST data:', request.POST)
        print('FILES data:', request.FILES)
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('author:profile')
    else:
        form = AvatarUploadForm(instance=request.user.profile)
    return render(request, 'upload_avatar.html', {'form': form})
@login_required
def profile(request):
    print (request.user.profile.avatar.url)
    return render(request, 'profile.html', {'user': request.user})