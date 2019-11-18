from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from .forms import RegForm
from .forms import LoginForm
def Home(request):
    return  render(request,'home.html')
def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Registration Successful')
    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})
def login(request):
    if request.method=='POST':
        MyLoginForm=LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un=MyLoginForm.cleaned_data['User']
            pw=MyLoginForm.cleaned_data['Pwd']
            dbuser=Reg.objects.filter(User=un,Pwd=pw)
            if dbuser:
                return  HttpResponse('Login successfully')
            else:
                return HttpResponse('Login Failed')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
        # Create your views here.
