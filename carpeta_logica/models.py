from django.db import models

class Calculo(models.Model):
    operacion = models.CharField(max_length=100)
    resultado = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
