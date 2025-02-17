from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import LoginForm, CadastroForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                return redirect("home:home")
            else:
                messages.error(request, "Email ou senha inválidos.")

    return render(request, "login.html", {"form": form})


def register(request):
    form = CadastroForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["password"]

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, "Este e-mail já está cadastrado!")
            else:
                usuario = Usuario.objects.create_user(username=nome, email=email, password= senha)
                usuario.save()

                messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
                return redirect('usuario:login')

    return render(request, 'register.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect("usuario:login")

@login_required
def editar_perfil(request):
    if request.method == "POST":
        novo_nome = request.POST.get('nome')
        nome_atual = request.user.username
        novo_email = request.POST.get('email')
        email_atual = request.user.email

        if nome_atual != novo_nome:
            request.user.username = novo_nome
            request.user.save()
            messages.success(request, "Perfil alterado com sucesso!")
            return redirect("usuario:editar_perfil")
        if email_atual != novo_email:
            request.user.email = novo_email
            request.user.save()
            messages.success(request, "Perfil alterado com sucesso!, Por favor, faça login novamente!")
            return redirect("usuario:login")

        senha = request.POST.get('senha')
        nova_senha = request.POST.get('nova_senha')
        confirmar_nova_senha = request.POST.get('confirmar_senha')

        if senha and nova_senha and confirmar_nova_senha:
            senha_atual = request.user.password

            if not check_password(senha, senha_atual):
                messages.error(request, "A senha fornecida não coincide com a atual!")
        
            elif nova_senha != confirmar_nova_senha:
                messages.error(request, "As senhas fornecidas não são iguais")

            else:
                request.user.password = make_password(nova_senha)
                request.user.save()
                messages.success(request, "Perfil alterado com sucesso!, Por favor, faça login novamente com sua nova senha")
                return redirect("usuario:login")
                
    return render(request, 'editar_perfil.html')