from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from loginwithauth.forms import UserLoginForm,UserRegistrationForm
#from loginwithauth.models import admin
#from django.views.generic import TemplateView
from django import forms
from django.contrib.auth import (authenticate, login ,get_user_model,logout)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def show(request):
    return render(request,'admin/base_site.html')

@login_required
def dashboardView(request):

    return render(request,'dashboard.html')



def login_view(request):
        if request.method =='POST':
                next = request.GET.get('next')
                form2 = UserLoginForm(request.POST)
                if form2.is_valid():
               # if request.method =='POST':

                        username = form2.cleaned_data.get('username')
                        password = form2.cleaned_data.get('password')
                        user = authenticate( username=username, password=password)
                        login(request,user)
                        if next:
                                return redirect (next)

                        return render(request,'admin/base_site.html')
                else:
                         return render(request,"registration/login.html",{'form': form2})

        else:
                form2 = UserLoginForm()
                return render(request,"registration/login.html",{'form': form2})
                        


                


def register(request):
        if request.method =='POST':
                form1 = UserRegistrationForm(request.POST)
                if form1.is_valid():

                        user = form1.save(commit=False)
                        username = form1.cleaned_data['username']
                        email = form1.cleaned_data['email']
                        psw = make_password(form1.cleaned_data['password'])
                        psw_confirm = form1.cleaned_data['confirm_password']


                                        
                        user = User(username=username,email=email,password=psw,is_staff=True)
                        user.save()
                        user = authenticate( username=username, password=psw)
                        login(request,user)
                        return render(request,'admin')

                        #return render(request,"registration/register.html",{'form': form1})

                
                else:
                        return render(request,"registration/register.html",{'form': form1})

                        
        else:
           form1 = UserRegistrationForm()
           return render(request,"registration/register.html",{'form': form1})




#.def registerView(request):
    # form = UserCreationForm(request.POST)
        #if form.is_valid():
           # form.save()
            #return redirect('login_url')
    #else:
            #form = UserCreationForm()
   # return render(request,'registration/register.html',{'form': form})
