from django import forms
from .models import Alimentos

class AdicionarAlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ["nome", "quantidade"]
        labels = {
            "nome": "Nome do Alimento",
            "quantidade": "Quantidade",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Nome..."}),
            "quantidade": forms.TextInput(attrs={"placeholder": "Quantidade..."})
        }

class DeletarAlimentoForm(forms.Form):
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
