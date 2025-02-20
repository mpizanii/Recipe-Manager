from django.shortcuts import render, redirect
from .forms import AdicionarReceitaForm, EditarReceitaForm, GeminiReceitaForm
from .models import Receitas
from django.contrib.auth.decorators import login_required
import re, os
import google.generativeai as genai
from home.models import Alimentos
from dotenv import load_dotenv

load_dotenv()

@login_required
def receita(request, receita_id):
    receita = Receitas.objects.get(id=receita_id)
    form_editar_receita = editar_receita(request = request, receita_id = receita_id)
    lista_ingredientes = get_ingredientes(receita_id)
    lista_modo_preparo = get_modo_preparo(receita_id)

    return render(request, 'receitas.html', 
                  {"receita": receita, 
                   "form_editar_receita": form_editar_receita, 
                   "lista_ingredientes": lista_ingredientes, 
                   "lista_modo_preparo": lista_modo_preparo
                })

def adicionar_receita(request):
    form = AdicionarReceitaForm()

    if request.method == "POST":
        form = AdicionarReceitaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            ingredientes = form.cleaned_data["ingredientes"]
            modo_preparo = form.cleaned_data["modo_preparo"]
            usuario_id = request.user.id

            receita = Receitas.objects.create(nome = nome, ingredientes = ingredientes, modo_preparo = modo_preparo, usuario_id = usuario_id)
            receita.save()
            
            form = AdicionarReceitaForm()
        
    return form

def editar_receita(request, receita_id):
    receita = Receitas.objects.get(id = receita_id)
    form = EditarReceitaForm(request.POST or None, instance = receita)

    if request.method == "POST":
        if form.is_valid():
            receita.save()

            return redirect('receitas:receita', receita_id = receita_id )
        
    return form

@login_required
def deletar_receita(request, receita_id):
    if request.method == "POST":
        Receitas.objects.filter(id = receita_id).delete()

    return redirect("home:home")

def get_ingredientes(id):
    receita = Receitas.objects.get(id = id)

    lista_ingredientes = [item.strip() for item in re.split(r'\d+[-.:]\s*', receita.ingredientes) if item.strip()]

    ingredientes_formatados = "\n".join(f'{i}: {ingrediente}.' for i, ingrediente in enumerate(lista_ingredientes, 1))

    return ingredientes_formatados

def get_modo_preparo(id):
    receita = Receitas.objects.get(id = id)

    lista_modo_preparo = [passo.strip() for passo in re.split(r'\d+[-.:]\s*', receita.modo_preparo) if passo.strip()]

    passos_formatados = "\n".join([f'Passo {i}: {passo}.' for i, passo in enumerate(lista_modo_preparo, 1)])

    return passos_formatados

def get_nome_receita_ia(texto):
    nome = re.search(r"Nome da receita:\s*(.*)", texto)
    return nome.group(1) if nome else None

def get_ingredientes_receita_ia(texto):
    ingredientes = re.search(r"Ingredientes:\s*(.*?)(Modo de preparo:|$)", texto, re.DOTALL)
    return ingredientes.group(1).strip() if ingredientes else None

def get_modo_preparo_receita_ia(texto):
    preparo = re.search(r"Modo de preparo:\s*(.*)", texto, re.DOTALL)
    return preparo.group(1).strip() if preparo else None

@login_required
def salvar_receita_ia(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        ingredientes = request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')
        usuario_id = request.user.id

        receita = Receitas.objects.create(nome = nome, ingredientes = ingredientes, modo_preparo = modo_preparo, usuario_id = usuario_id)
        receita.save()

        return redirect('home:home')

@login_required  
def receita_ia(request):
    usuario_id = request.user.id
    form = GeminiReceitaForm(request.POST or None, usuario_id = usuario_id)
    gemini_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-pro")

    if request.method == "POST":
        if form.is_valid():
            alimentos = form.cleaned_data["alimentos"]

            nomes_alimentos = [(alimento.nome, alimento.quantidade) for alimento in Alimentos.objects.filter(id__in = alimentos).all()]

            pergunta = (
                "Responda apenas seguindo esse padrão (aonde tiver '\n' quebre uma linha):"
                "Nome da receita: (Nome da receita)\n"
                "Ingredientes: (1- (Ingrediente 1)\n2- (Ingrediente 2)\n3- ...)"
                "Modo de preparo: (1- (Passo 1)\n2- (Passo 2)\n3- ...\n\n"
                f"Faça uma receita, seguindo o padrão já mencionado, com APENAS os seguintes alimentos (não precisa utilizar todos): {nomes_alimentos}"
                )
            
            response = model.generate_content(pergunta)

            receita_texto = response.text

            nome = get_nome_receita_ia(receita_texto)
            ingredientes = get_ingredientes_receita_ia(receita_texto)
            modo_preparo = get_modo_preparo_receita_ia(receita_texto)

            return render(request, 'receita_ia.html',
                        {"nome": nome,
                        "ingredientes": ingredientes,
                        "modo_preparo": modo_preparo,
                        })
    return form