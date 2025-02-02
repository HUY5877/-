from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()
class Blogkind(models.Model):
    name = models.CharField(max_length=120, verbose_name='分类名称')
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
    # def __str__(self):
    #     return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200 , verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True , verbose_name='发布时间')
    kind = models.ForeignKey(Blogkind, on_delete=models.CASCADE , verbose_name='分类名称')
    author = models.ForeignKey(user, on_delete=models.CASCADE , verbose_name='作者')
    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"
        ordering = ['-pub_time']
    # def __str__(self):
    #     return self.title

class Comment(models.Model):
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE ,related_name='comments', verbose_name='所属博客')
    author = models.ForeignKey(user, on_delete=models.CASCADE , verbose_name='作者')
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ['-pub_time']
    # def __str__(self):
    #     return self.author