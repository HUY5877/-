import profile

from django.urls import path
from .views import *

app_name = 'author'
urlpatterns = [
    path('login', login1, name="login"),
    path('register', register, name="register"),
    path('sendemail', send_yanzheng, name="send_yanzheng"),
    path('out', out, name="out"),
    path('profile', profile, name='profile'),
    path('upload_avatar', upload_avatar, name='upload_avatar'),
]
