from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        usuario = authenticate(request, username = email, password = senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha incorreto. Tente novamente.")
            return redirect('usuario:login')
        
    return render(request, 'login.html', {"messages":messages})

