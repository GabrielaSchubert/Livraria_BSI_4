from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    