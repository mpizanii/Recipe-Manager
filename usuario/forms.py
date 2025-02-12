from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Usuário",
        widget=forms.TextInput(attrs={'placeholder': 'Usuário'})
    )
    password = forms.CharField(
        label = "Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )