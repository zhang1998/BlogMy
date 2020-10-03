from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):#2
    if request.method=="POST":#3
        login_form=LoginForm(request.POST)#4
        if login_form.is_valid():#5
            cd=login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])#7

            if user:
                login(request,user)#8
                return HttpResponse("Wellcome You. authenticated successfully")#9
            else:
                return HttpResponse("Sorry, your username or password is not right")
        else:
            return HttpRespnse("Invalid login")
    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def register(request):
    if request.method=="POST":
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False) #1
            new_user.set_password(user_form.cleaned_data['password'])#2
            new_user.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry,you can not register")
    else:
        user_form=RegistrationForm()
        return render(request,"account/register.html",{"form":user_form})
