from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('home/', include('home.urls')),
    path('receitas/', include('receitas.urls'))
]