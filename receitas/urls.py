from django.urls import path
from . import views

app_name = 'receitas'

urlpatterns = [
    path('', views.receita, name='receitas'),
]