from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import templates
from .models import IssueModel
from django.contrib.auth.forms import UserCreationForm,User
# Create your views here.

def index(request):
    issue_list=IssueModel.objects.values()
    return render(request,template_name='index.html',context={'list':issue_list})

def add(request):
    data=request.POST.dict().copy()
    obj=IssueModel(desc=data.get("desc"),type=data.get("issuetype"),created_on=data.get("rdate"),created_by=data.get("creator"),logged_by=data.get("logger"),environment=data.get("envname"))
    obj.save()
    return render(request,template_name='success.html',context={'id':obj.pk})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})
