from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm

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


class EditarPerfilForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditarPerfilForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    password = None

    class Meta:
        model = Usuario
        fields = ['username', 'email']

class EditarSenhaForm(forms.Form):
    senha = forms.CharField(
        label="Senha Atual",
        widget=forms.PasswordInput(attrs={"placeholder": "Senha Atual..."}),
        required=False,
    )
    nova_senha = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Nova Senha..."}),
        required=False,
    )
    confirmar_senha = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmar Senha..."}),
        required=False,
    )