from django import forms
from .models import Receitas
from home.models import Alimentos

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

class EditarReceitaForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = ["nome", "ingredientes", "modo_preparo"]
        labels = {
            "nome": "Nome",
            "ingredientes": "Ingredientes",
            "modo_preparo": "Modo de Preparo",
        }
        widgets = {
            "nome": forms.TextInput(),
            "ingredientes": forms.Textarea(attrs={"rows": 4, "cols": 20}),
            "modo_preparo": forms.Textarea(attrs={"rows": 4, "cols": 20}),
        }   

class GeminiReceitaForm(forms.Form):
    alimentos = forms.ModelMultipleChoiceField(
        queryset=Alimentos.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = "Alimentos"
    )

    def __init__(self, *args, usuario_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario_id:
            self.fields['alimentos'].queryset = Alimentos.objects.filter(usuario_id=usuario_id)