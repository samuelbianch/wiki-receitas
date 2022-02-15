from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.TextField(max_length=100)
    data_receita = models.DateField(datetime.now(), blank=True)
