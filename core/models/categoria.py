from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100, verbose_name= "descrição")
    
    def __str__(self):
        return self.descricao