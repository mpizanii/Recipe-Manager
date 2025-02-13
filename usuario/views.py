from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import CustomLoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            usuario = authenticate(username = username, password = password)

            if usuario is not None:
                print('autenticado')
                login(request, usuario)
                return redirect('home:home')
            else:
                print("não autenticado")
                messages.error(request, "Credenciais incorretas. Tente novamente!")
    else:
        print('invalido')
        form = CustomLoginForm()
        
    return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            confirmar_senha = request.form['confirmar_senha']

            usuario_existente = User.objects.get(email = email)

            if usuario_existente:
                messages.error(request, "Este e-mail já está cadastrado")
            
            elif senha != confirmar_senha:
                messages.error(request, "Senhas não coincidem!")
            

            return redirect('usuario:login')

    return render(request, 'register.html')


