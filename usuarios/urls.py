from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('criar/cria-receita', views.cria_receita, name='cria_receita')
]
