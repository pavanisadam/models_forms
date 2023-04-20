from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic inserted succesfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WPFO=WebpageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('webpage inserted succesfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        APFO=AccessRecordForm(request.POST)
        if APFO.is_valid():
            APFO.save()
            return HttpResponse('accesrecord inserted succesfully')


    return render(request,'insert_access.html',d)
