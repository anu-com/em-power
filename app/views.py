from django.shortcuts import render
from .models import *
# Create your views here.
def regView(request):
    return render(request,'app/reg.html')

def regData(request):
    if request.method == 'POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        newdata=student.objects.filter(Email=email)
        if newdata:
            message='user already registered'
            return render(request,'app/reg.html',{'msg':message})
        else:
            if password==cpassword:
                ndata=student.objects.create(Username=username,Email=email,Password=password)
                message='user successfully register'
                return render(request,'app/login.html',{'msg':message})
            else:
                message="user doesn't exist"
                return render(request,'app/reg.html',{'msg':message})
def loginView(request):
    return render(request,'app/login.html')

def loginData(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        ldata=student.objects.get(Email=email)
        if ldata:
            request.session['Username']=ldata.Username
            request.session['Email']=ldata.Email
            request.session['Password']=ldata.Password
            if ldata.Password==password:
                return render(request,'app/index.html')
            else:
                message='password incorrect'
                return render(request,'app/login.html',{'msg':message})

def about(request):
    return render(request,"app/about.html")

def service(request):
    return render(request,"app/service.html")

def contact(request):
    return render(request,"app/contact.html")