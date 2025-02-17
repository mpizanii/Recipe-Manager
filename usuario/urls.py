from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
]