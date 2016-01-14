from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'forumsite/forumIndex.html')


def thread(request,threadid):
    return render(request,'forumsite/thread.html')


def login(request):
    user = authenticate(username=request.POST['useraccount'],password=request.POST['password'])
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            _temp_user = User.objects.get(username=request.POST['useraccount'])
            if _temp_user is not None:
                print '****** userid = ' ,_temp_user.id
            else:
                print '****** no username = ' ,request.POST['useraccount']
            return redirect('/')
        else:
            return HttpResponse("the password is valid , but the account has been disabled!")
    else:
        return HttpResponse("the username and password were incorrent.")
        

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    
    if password1 != password2:
        return HttpResponse("password not the same , please retry!")
    newuser = User.objects.create_user(username,email,password1)
    if newuser is None:
        return HttpResponse("register failed, please try agagin !")
    else:
        _tempUser = authenticate(username=username,password=password1)
        
        print '****** , username:', _tempUser.username
        
        auth_login(request,_tempUser)
        return redirect('/')
    
    
    


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    response = render(request,'forumsite/forumIndex.html')
    response.delete_cookie('user')
    
    return response
        

@login_required(login_url='/login/')
def login_require(request):
    return HttpResponse("congrautuations , you have logined.")



def committhreads(request):
    return render(request,'forumsite/post.html')