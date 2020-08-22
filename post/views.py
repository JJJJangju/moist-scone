from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import Postform
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def main(request):
    blog=Post.objects.all().order_by('-id')
    return render(request, 'main.html', {'blog':blog})

def detail(request, blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def create(request):
    if request.method=="POST":
        blog=Post()
        blog.user = request.user
        blog.title=request.POST['title']
        try:
            blog.image=request.FILES['image']
        except:
            pass
        blog.body=request.POST['body']
        blog.save()
        return redirect('/detail/' + str(blog.id))
    return render(request, 'new.html')

def update(request, blog_id):
    if request.method=="POST":
        blog=get_object_or_404(Post, pk = blog_id)
        blog.title=request.POST['title']
        try:
            blog.image=request.FILES['image']
        except:
            pass
        blog.body=request.POST['body']
        blog.save()
        return redirect('/detail/' + str(blog.id))
    blog=get_object_or_404(Post, pk=blog_id)
    return render(request, 'renew.html', {'blog':blog})

def delete(request, blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    blog.delete()
    return redirect('/')



def likes(request): 
    if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
        blog_id = request.GET['blog_id'] #좋아요를 누른 게시물id (blog_id)가지고 오기
        post = Post.objects.get(id=blog_id)
        
        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
            message = "로그인을 해주세요" #화면에 띄울 메세지 
            context = {'like_count' : post.like.count(),"message":message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user #request.user : 현재 로그인한 유저
        if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
            post.like.remove(user) #like field에 현재 유저 추가
            message = "좋아요 취소" #화면에 띄울 메세지
        else: #좋아요를 누르지 않은 유저일 때
            post.like.add(user) #like field에 현재 유저 삭제
            message = "좋아요" #화면에 띄울 메세지
        # post.like.count() : 게시물이 받은 좋아요 수  
        context = {'like_count' : post.like.count(),"message":message}
        return HttpResponse(json.dumps(context), content_type='application/json')
