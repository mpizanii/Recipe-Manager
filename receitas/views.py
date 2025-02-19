from django.shortcuts import render, redirect
from .forms import AdicionarReceitaForm
from .models import Receitas

def receita(request):
    ...

def adicionar_receita(request):
    form = AdicionarReceitaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            ingredientes = form.cleaned_data["ingredientes"]
            modo_preparo = form.cleaned_data["modo_preparo"]
            usuario_id = request.user.id

            receita = Receitas.objects.create(nome = nome, ingredientes = ingredientes, modo_preparo = modo_preparo, usuario_id = usuario_id)
            receita.save()

            return redirect('home:home')
        
    return form
