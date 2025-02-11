from django.db import models


class Pessoas(models.Model):
    nome = models.TextField(max_length=100)
    idade = models.IntegerField()
