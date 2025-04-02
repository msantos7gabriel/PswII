from django.db import models


class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    porte_de_arma = models.BooleanField()
    nascimento = models.DateField()
