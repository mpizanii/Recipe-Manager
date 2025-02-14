from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    first_name = None
    last_name = None
    last_login = None
    username = models.CharField(unique=False, max_length=200)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email