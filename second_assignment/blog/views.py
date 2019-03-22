from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
        blogs = Blog.objects    # queryset
        return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, blog_id):
    if request.method == 'GET':
        # pk(primary key)란, 모델에서 찍어낸 객체들 간의 구분자. 데이터를 구분 지을 수 있는 이름표
        blog_detail = get_object_or_404(Blog, pk=blog_id)   # 'object를 가져오고 없으면 404 오류를 띄워라'라는 함수
        return render(request, 'blog/detail.html', {'blog': blog_detail})
    elif request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.title = request.POST['title']
        blog.pub_date = timezone.datetime.now()
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blog/' + str(blog.id))

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title =  request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/edit.html', {'blog': blog_detail})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')
