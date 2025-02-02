from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST
from .models import *
from .forms import *
from django.http.response import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request ):
    # if not blogs:
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    try :
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    # print(page , len(blogs))
    return render(request, 'index.html' , context={'blogs':blogs})


def blog_detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request, 'blog_detail.html' ,context={'blog':blog})


@login_required(login_url='/author/login')
@require_http_methods(['GET', 'POST'])
def pub_blog(request):
    if request.method == 'GET':
        kind = Blogkind.objects.all()
        # 渲染全部的类型
        return render(request, 'pub_blog.html',context={'kind':kind})
    else :
        form = PubBlogForm(request.POST)
        if form.is_valid():
            kind_id = form.cleaned_data['kind']
            content = form.cleaned_data['content']
            title = form.cleaned_data['title']
            # 这里传kind_id
            blog = Blog.objects.create(kind_id=kind_id, content=content, title=title ,author=request.user)

            return JsonResponse({'code': '200' , 'message': '博客发布成功!!!','data': {'blog_id':blog.id} })
        else:
            print(form.errors)
            return JsonResponse({'code': '400', 'message': '表单验证失败'})

@require_http_methods(['GET', 'POST'])
@login_required(login_url='/author/login')
def pub_comment(request):
    if request.method == 'GET':
        content = request.GET.get('content')
        if content:
            return JsonResponse({'code':200})
        else:
            return JsonResponse({'code':400})
    else :
        content = request.POST.get('content')
        blog_id = request.POST.get('blog_id')
        # print(content , blog_id)
        comment = Comment.objects.create(content=content , author=request.user , blog_id=blog_id)
        # res = reverse('blog:detail' , args=[1])
        return redirect(reverse('blog:detail', kwargs={'blog_id': blog_id}) )
@require_http_methods(['GET'])
def search_blog(request):
    # blogs = Blog.objects.all()
    inf = request.GET.get('inf')
    print(inf)
    blogs = Blog.objects.filter(Q(title__icontains=inf) | Q(content__icontains=inf)  )
    # print(len(blogs) , reverse('blog:index'))
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    # print(page , len(blogs))
    return render(request , 'index.html' , context={'blogs':blogs})
