from django.contrib import admin
from .models import Pessoa

class Listando_Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15

admin.site.register(Pessoa, Listando_Pessoas)
