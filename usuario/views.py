from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(username = email, password = senha)

        print(usuario)

        if usuario is not None:
            print(usuario)
            login(request, usuario)
            return redirect('home:home')
        else:
            print("Autenticação falhou:", usuario)
            messages.error(request, "Credenciais incorretas. Tente novamente!")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem!")
            return render(request, 'register.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado!")
            return render(request, 'register.html')

        usuario = Usuario.objects.create_user(username=nome, email=email, password= senha)
        usuario.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return redirect('usuario:login')

    return render(request, 'register.html')


