from django.urls import path

from .views import  *
app_name = 'blog'
urlpatterns = [
    path('' , index , name="index"),
    path('blog/<int:blog_id>' , blog_detail , name="detail"),
    path('pub' , pub_blog , name="pub_blog"),
    path('pub_comment' , pub_comment , name="pub_comment"),
    path('search_blog' , search_blog , name="search_blog"),
]