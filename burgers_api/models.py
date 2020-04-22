from django.db import models

# Create your models here.
class Ingredientes(models.Model):
  nombre = models.CharField(max_length=60)
  descripcion = models.CharField(max_length=60)

  def __str__(self):
    return self.nombre


class Hamburguesa(models.Model):
  nombre = models.CharField(max_length=60)
  precio = models.IntegerField()
  descripcion = models.CharField(max_length=60)
  imagen = models.CharField(max_length=100)
  ingredientes = models.ManyToManyField(Ingredientes, blank=True)
  
  def __str__(self):
    return self.nombre


