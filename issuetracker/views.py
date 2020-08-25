from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from . import templates
from django.contrib.auth import authenticate
from django.contrib.auth.admin import User
from .serializer import IssueModelSerializer
from .models import IssueModel
from rest_framework import request
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.forms import UserCreationForm,User
# Create your views here.

class GenericView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=IssueModelSerializer
    queryset=IssueModel.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

@api_view(['POST'])
def get_token(request):
    user=authenticate(username=request.data['username'],password=request.data['password'])
    if user:
        token =Token.objects.get(user=user)
        print(token)
        return JsonResponse({"token":token.key},safe=False)
    else:
        return JsonResponse({"token":"null"})



def rest_view(request):
    issue_list=IssueModel.objects.values()
    serailizer=IssueModelSerializer(issue_list,many=True)
    return JsonResponse(serailizer.data,safe=False)

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
