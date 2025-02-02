from django.contrib import admin

# Register your models here.
from .models import *
class BlogkindAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content' , 'pub_time' , 'kind' , 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author' , 'content' , 'pub_time' , 'blog_id']
admin.site.register(Blogkind, BlogkindAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)