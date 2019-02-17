from django.shortcuts import render
from .models import * 
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"app/dashboard.html")

def loginpage(request):
    return render(request,"app/login.html")

def registerpage(request):
    return render(request,"app/register.html")

def registeruser(request):
    obj=user()
    obj.name=request.POST['name']
    obj.email=request.POST['email']
    obj.password=request.POST['password']
    enter=user.objects.create(name= obj.name,email=obj.email,password=obj.password)
    return render(request,"app/login.html")

def login_check(request):
    try:
        email=request.POST['email']     
        password=request.POST['password']
        u_data=user.objects.get(email=email)
        if u_data:
            if u_data.email==email and u_data.password==password:
                getall=task.objects.all()
                request.session['name']=u_data.name
                return render(request,"app/dashboard.html",{'getall':getall,'u_data':u_data})
            else:
                return render(request,"app/login.html")      
        else:
           return render(request,"app/login.html")
    except user.DoesNotExist:
        return render(request,"app/login.html")

def post_task(request):
    obj=task()
    obj.user_id=request.POST['username']
    obj.desc=request.POST['desc']
    post_task_data=task.objects.create(username=obj.user_id,desc=obj.desc)
    getall=task.objects.all()
    return render(request,"app/dashboard.html",{'getall':getall})


    