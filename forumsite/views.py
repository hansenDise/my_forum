from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'forumsite/forumIndex.html')


def thread(request,threadid):
    print 'threadid is :', threadid
    return render(request,'forumsite/thread.html')


def login(request):
    for key in request.POST:
        print 'key = ',key
    return HttpResponse("data posted success..")    
    
        

def register(request):
    pass