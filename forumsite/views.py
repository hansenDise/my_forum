from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import hashlib
import datetime

from django.core.exceptions import ObjectDoesNotExist

from forumsite.models import Category,Thread,Comment
# Create your views here.

def index(request):
    threads = Thread.objects.all()[0:19]
    categories = Category.objects.all()
    return render(request,'forumsite/forumIndex_test.html',{'threads':threads,'categories':categories})


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
    
    return redirect('/')

#@login_required(login_url='/login/')
#def login_require(request):
#    return HttpResponse("congrautuations , you have logined.")


def committhreads(request):
    categories = Category.objects.all()
    return render(request,'forumsite/post.html',{'categories':categories})

def commit_thread(request):
    if request.user.is_authenticated():
        try:
            user = User.objects.get(username=request.user.username)
            if user is None:
                # return Error Page.
                return HttpResponse("Error: user does not exists.")
            else:
                form_title = request.POST['title']
                form_content = request.POST['content']
                form_category = request.POST['category']    
                category = Category.objects.get(categoryid=form_category)
                
                hashobj = hashlib.sha1()
                encodestr = user.username + str(datetime.datetime.now())
                hashobj.update(encodestr)
                hashcode = hashobj.hexdigest()[0:7]
                
                thread = Thread(categoryid=category,title=form_title,content=form_content,userid=user,hashcode=hashcode)
                thread.save()

                # return to this thread page
                return redirect('/')
                
        except Exception as e:
            return HttpResponse(e.args + e.mro)
    else:
        # return user not login page.
        return HttpResponse("you are not login. please login.")

def threadsAll(request):
    return redirect('/')

def threadCate(request,threadType):
    categories = Category.objects.all()
    threads = Thread.objects.filter(categoryid=Category.objects.get(nameEN=threadType))
    return render(request,'forumsite/forumIndex_test.html',{'threads':threads,'categories':categories})

def getThread(request,threadType,threadid):
    categories = Category.objects.all()
    thread = Thread.objects.get(hashcode=threadid)
    return render(request,'forumsite/thread.html',{'thread':thread,'categories':categories})
    

def notfound(request):
    raise Http404("Page Not Found...")
    
def checkusername(request):
    ret = 0
    try:
        uname = request.GET['username']
        user = User.objects.get(username=uname)
        if user is not None:
            ret = 1
    except ObjectDoesNotExist:
        pass
    return HttpResponse(str(ret))