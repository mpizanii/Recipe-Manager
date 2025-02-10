from django.db import models
from usuario.models import Usuario

class Alimentos(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=80)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='alimentos')

    def __str__(self):
        return self.nome

class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receitas')

    def __str__(self):
        return self.nome
