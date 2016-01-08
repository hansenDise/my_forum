from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        print 'not login'
    else:
        print 'already login'
    return render(request,'forumsite/forumIndex.html')


def thread(request,threadid):
    print 'threadid is :', threadid
    return render(request,'forumsite/thread.html')


def login(request):
    print 'username =', request.POST['useraccount'] , ' password = ', request.POST['password']
    user = authenticate(username=request.POST['useraccount'],password=request.POST['password'])
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return redirect('/')
        else:
            return HttpResponse("the password is valid , but the account has been disabled!")
    else:
        return HttpResponse("the username and password were incorrent.")
        

def register(request):
    for key in request.POST:
        print key , ' = ', request.POST[key]
        
    return HttpResponse("in register page.")


def logout_view(request):
    print '******* in logout*************'
    if request.user.is_authenticated():
        print 'authenticated'
        logout(request)
        return redirect('/')
    else:
        print 'not authen.'
        return redirect('/')
        

@login_required(login_url='/login/')
def login_require(request):
    return HttpResponse("congrautuations , you have logined.")