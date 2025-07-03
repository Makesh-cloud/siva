from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    obj=User.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        userpassword=request.POST['password']

        for i in obj:
            if i.name==username:
                if i.password==userpassword:
                    messages.error(request, "logined sucessfully")
                    return redirect('home')
                else:
                    messages.error(request, "password not match")
                    return redirect('login')
        if request.method=='POST':
            messages.error(request, "username not found")
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):
    obj=User.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        mail=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            result='true'
            for i in obj:
                if i.name!=username:
                    result='true'
                else:
                    result='false'
            if result=='true':
                obj=User(name=username, email=mail, password=password)
                obj.save()
                return redirect('login')
            else:
                messages.error(request, "username already existed")
                return redirect('register')
                
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
    
    else:
        return render(request,'register.html')