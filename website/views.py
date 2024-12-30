from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms  import SignUpForm
# Create your views here.


def home(request) :
    if request.method == 'POST' :
        username = request.POST['username'];
        password = request.POST['password'];
        # Authentiaction
        user= authenticate(request,username=username,password=password);
        if user is not None :
            login(request,user);
            messages.success(request,'You Have Been Logged In !')
            return redirect('home')
        else :
            messages.success(request,'There are A Wrong In Loogging, Please Try Agin')
            return redirect('home')
    else :
     return render(request,'home.html',{})

# def login_user(request) :
#     pass

def logout_user(request) :
    logout(request)
    messages.success(request,'You Have Been Logged Out  Thank You')
    return redirect('home')



def regiser_user(request) :
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You Have success Regiser')
            return  redirect('home')
    else :
       form = SignUpForm()
       return render(request,'regiser.html',{'form':form})



