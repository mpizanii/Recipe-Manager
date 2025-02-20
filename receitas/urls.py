from django.urls import path
from . import views

app_name = 'receitas'

urlpatterns = [
    path('<int:receita_id>/', views.receita, name='receita'),
    path('<int:receita_id>/edit', views.editar_receita, name='editar_receita'),
    path('<int:receita_id>/delete', views.deletar_receita, name='deletar_receita'),
    path('receita_gerada/', views.receita_ia, name='receita_ia'),
    path('salvar_receita/', views.salvar_receita_ia, name = 'salvar_receita_ia')
]