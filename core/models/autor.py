from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
