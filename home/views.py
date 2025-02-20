from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Alimentos
from receitas.models import Receitas
from .forms import AdicionarAlimentoForm, DeletarAlimentoForm
from receitas.views import adicionar_receita, receita_ia


@login_required
def home_view(request):
    nome_usuario = request.user.username.capitalize()
    usuario_id = request.user.id
    alimentos = Alimentos.objects.filter(usuario_id = usuario_id).all()
    receitas = Receitas.objects.filter(usuario_id = usuario_id).all()
    form_adicionar_alimentos = adicionar_alimento(request)
    form_deletar_alimentos = deletar_alimento(request)
    form_adicionar_receitas = adicionar_receita(request)
    form_receita_ia = receita_ia(request)

    return render(request, 'home.html', 
                  {"nome_usuario": nome_usuario, 
                   "alimentos": alimentos, 
                   "receitas": receitas,
                   "form_adicionar_alimentos": form_adicionar_alimentos,
                   "form_deletar_alimentos": form_deletar_alimentos,
                   "form_adicionar_receitas": form_adicionar_receitas,
                   "form_receita_ia": form_receita_ia
                })

def adicionar_alimento(request):
    form = AdicionarAlimentoForm()

    if request.method == "POST":
        form = AdicionarAlimentoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            quantidade = form.cleaned_data["quantidade"]
            usuario_id = request.user.id

            alimento = Alimentos.objects.create(nome = nome, quantidade = quantidade, usuario_id = usuario_id)
            alimento.save() 

            form = AdicionarAlimentoForm()

    return form

def deletar_alimento(request):
    usuario_id = request.user.id
    form = DeletarAlimentoForm(usuario_id= usuario_id)

    if request.method == "POST":
        form = DeletarAlimentoForm(request.POST, usuario_id= usuario_id)
        if form.is_valid():
            alimentos_selecionados = form.cleaned_data["alimentos"]

            alimentos_para_deletar = [alimento.id for alimento in alimentos_selecionados]

            Alimentos.objects.filter(id__in = alimentos_para_deletar).delete()

            form = DeletarAlimentoForm(usuario_id= usuario_id)
            
    return form
