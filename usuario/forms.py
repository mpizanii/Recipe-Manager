from django import forms
from .models import Usuario

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "E-mail..."})
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Senha..."})
    )

class CadastroForm(forms.ModelForm):
    confirmar_senha = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmar Senha..."})
    )
    class Meta:
        model = Usuario
        fields = ["username", "email", "password"]
        labels = {
            "username": "Nome",
            "email": "E-mail",
            "password": "Senha",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Nome..."}),
            "email": forms.EmailInput(attrs={"placeholder": "E-mail..."}),
            "password": forms.PasswordInput(attrs={"placeholder": "Senha..."}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("password")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error("confirmar_senha", "As senhas não coincidem")

        return cleaned_data