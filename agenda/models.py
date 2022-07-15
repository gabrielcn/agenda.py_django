from django.db import models

# Create your models here.
class Evento(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    titulo = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(null=False)
    data_criacao = models.DateTimeField(auto_now=True)