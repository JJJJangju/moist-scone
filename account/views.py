from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):    
    if request.method == 'POST': #값이 넘겨졌을 경우
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    # if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    # return redirect('/')    
    
def myprofile(request,user_id):  
    user = User.objects.get(id = user_id)
    post_likes = user.likes.all()
    context={
        "post_likes":post_likes,
    }
    return render(request, 'myprofile.html',context)