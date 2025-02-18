from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import LoginForm, CadastroForm, EditarPerfilForm, EditarSenhaForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.forms import UserChangeForm
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
            confirmar_senha = form.cleaned_data["confirmar_senha"]

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, "Este e-mail já está cadastrado!")

            elif senha != confirmar_senha:
                messages.error(request, "Senhas não coincidem!")

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
    usuario = request.user
    senha_atual = usuario.password

    form_perfil = EditarPerfilForm(instance = usuario)
    form_senha = EditarSenhaForm()

    if request.method == "POST":
        if 'button_perfil' in request.POST:
            form_perfil = EditarPerfilForm(request.POST, instance=usuario)
            novo_email = request.POST.get("email")

            if Usuario.objects.filter(email=novo_email).exclude(id=usuario.id).exists():
                messages.error(request, "Este e-mail já está cadastrado!")
                return redirect("usuario:editar_perfil")
            
            if form_perfil.is_valid():
                form_perfil.save()
                messages.success(request, "Perfil alterado com sucesso! Por favor, faça login novamente!")
                return redirect("usuario:login")
        
        if 'button_senha' in request.POST:
            form_senha = EditarSenhaForm(request.POST or None)

            if form_senha.is_valid():
                senha = form_senha.cleaned_data["senha"]
                nova_senha = form_senha.cleaned_data["nova_senha"]
                confirmar_senha = form_senha.cleaned_data["confirmar_senha"]

                if not check_password(senha, senha_atual):
                    messages.error(request, "A senha fornecida não coincide com a atual!")
                    return redirect("usuario:editar_perfil")
            
                elif nova_senha != confirmar_senha:
                    messages.error(request, "As senhas fornecidas não são iguais!")
                    return redirect("usuario:editar_perfil")

                else:
                    request.user.password = make_password(nova_senha)
                    request.user.save()
                    messages.success(request, "Perfil alterado com sucesso!, Por favor, faça login novamente com sua nova senha!")
                    return redirect("usuario:login")

    return render(request, 'editar_perfil.html', {"form_perfil": form_perfil, "form_senha": form_senha})