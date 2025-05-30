import os
from dotenv import load_dotenv, find_dotenv
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm, CreateUserForm
from .models import User, MensagemContato
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    current_page = 'index'
    return render(request, "pages/home.html", {'current_page': current_page})

def about(request):
    current_page = 'sobre'
    return render(request, "pages/sobre.html", {'current_page': current_page})

def contato(request):
    current_page = 'contato'

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        assunto = request.POST.get("assunto")
        mensagem = request.POST.get("mensagem")
        email_empresa = os.environ["EMAIL_HOST_USER"]
        # Validar forumário e inserir no banco de dados
        send_mail(
                subject=assunto,
                message=mensagem,
                from_email=email,  # Usa o DEFAULT_FROM_EMAIL
                recipient_list=[email_empresa],
                fail_silently=False,
            )
        # return render(request, "pages/contato.html", {"success": True}, {'current_page': current_page})

    return render(request, "pages/contato.html", {'current_page': current_page})

def aviso(request):
    current_page = 'aviso'
    return render(request, "pages/aviso.html", {'current_page': current_page})

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
        messages.error(request, 'Email ou Senha inválida. Tente novamente.')
        return render(request, "pages/login.html")

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

            email = form.cleaned_data['email']
            print(email)
            
            send_mail(
                subject='Sua conta foi criada',
                message=f'usuário criado com sucesso\nsenha do usuário: {password}',
                from_email=None,  # Usa o DEFAULT_FROM_EMAIL
                recipient_list=[email],
                fail_silently=False,
            )
            return HttpResponse("Usuário criado com sucesso\nsenha do usuário: "+password)
    return render(request,"pages/create_user.html", {"form":form })
