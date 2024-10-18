from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm, CreateUserForm
from .models import User 

# Create your views here.
def index(request):
    return render(request, "index.html")

def loginview(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method != "POST":
        return render(request, "login.html")
    
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return HttpResponse("invalid credentials", status=401)
    
def create_user(request):
    if request.method =="GET":
        return render(request,"create_user.html", {"form": UserForm()})
    elif request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data["password"])
            form.save()
            return HttpResponse("Usuário criado com sucesso")
    return render(request,"create_user.html", {"form":form })

def create_user_adm(request):
    if request.method =="GET":
        return render(request,"create_user.html", {"form":CreateUserForm()})
    elif request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            password=(User.objects.make_random_password())
            form.instance.set_password(password)
            form.save()
            return HttpResponse("Usuário criado com sucesso\nsenha do usuário: "+password)
    return render(request,"create_user.html", {"form":form })