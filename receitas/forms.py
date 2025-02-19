from django import forms
from .models import Receitas

class AdicionarReceitaForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = ["nome", "ingredientes", "modo_preparo"]
        labels = {
            "nome": "Nome",
            "ingredientes": "Ingredientes",
            "modo_preparo": "Modo de Preparo",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Nome..."}),
            "ingredientes": forms.Textarea(attrs={"placeholder": "1-...\n2-...\n3-...", "rows": 4, "cols": 20}),
            "modo_preparo": forms.Textarea(attrs={"placeholder": "1-...\n2-...\n3-...", "rows": 4, "cols": 20}),
        }

class GeminiReceitaForm(forms.Form):
    ...