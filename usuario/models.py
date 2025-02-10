from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
