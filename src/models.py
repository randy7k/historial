from django.db import models

class Objetivo(models.Model):
    metrica = models.CharField(blank=False, max_length=30)
    descripcion = models.TextField(blank=False, max_length=150)

    def __str__(self):
        return self.metrica

class Consecucion(models.Model):
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    descripcion = models.CharField(blank=False, max_length=30)
    meta = models.FloatField(blank=False)
    porcentaje_de_consecucion = models.FloatField(blank=False)

    def __str__(self):
        return self.descripcion + " (" + str(self.objetivo) + ")"
