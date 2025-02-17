from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario

@login_required
def home_view(request):
    nome_usuario = request.user.username

    return render(request, 'home.html', {"nome_usuario": nome_usuario})
