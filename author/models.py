from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
User = get_user_model()
class yanzheng(models.Model):
    email = models.EmailField(unique=True)
    ma = models.CharField(max_length=4)
    create_time = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 与 User 模型一对一关联
    avatar = models.ImageField(
        upload_to='avatars/',  # 头像存储路径
        default='avatars/默认.jpg',  # 默认头像路径
        blank=True,
        null=True
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
