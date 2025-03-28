from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm, CreateUserForm
from .models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/sobre.html")

def contato(request):
    return render(request, "pages/contato.html")

def aviso(request):
    return render(request, "pages/aviso.html")

def loginview(request):
    if request.user.is_authenticated:
        return redirect("criar-usuario")
    if request.method != "POST":
        return render(request, "pages/login.html")
    
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return redirect("criar-usuario")
    else:
        return render(request, "login.html", context={"erro_message": "Usuário não cadastrado!"})

@login_required
def create_user(request):
    if request.method =="GET":
        return render(request,"pages/create_user.html", {"form": UserForm(instance=request.user)})
    elif request.method=="POST":
        form=UserForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
           # form.instance.set_password(form.cleaned_data["password"]) - senha não necessária 
            form.save()
            #return HttpResponse("Usuário criado com sucesso")
    return render(request,"pages/create_user.html", {"form":form })

@login_required
@user_passes_test(lambda u: u.groups.filter(name='adm').exists())
def create_user_adm(request):
    if request.method =="GET":
        return render(request,"pages/create_user.html", {"form":CreateUserForm()})
    elif request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            password=(User.objects.make_random_password())
            form.instance.set_password(password)
            form.save()
            return HttpResponse("Usuário criado com sucesso\nsenha do usuário: "+password)
    return render(request,"pages/create_user.html", {"form":form })

# @login_required
# def foto_perfil(request):
#     if request.method=="GET":
#         if request.user.is_authenticated:
#             with request.user.foto_cadastro.open("r") as f:
#                 return HttpResponse(f,content_type="image/jpg" )
#     return HttpResponse("error", status=401)