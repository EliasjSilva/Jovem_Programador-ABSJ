from django.db import models

class Curisosidade(models.Model):
    titulo = models.TextField()
    descricao = models.TextField()