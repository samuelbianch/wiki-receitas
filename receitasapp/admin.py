from django.contrib import admin
from .models import Receita

class Listando_Receitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_editable = ('publicada',)
    list_filter = ('categoria',)
    list_per_page = 15

admin.site.register(Receita, Listando_Receitas)
