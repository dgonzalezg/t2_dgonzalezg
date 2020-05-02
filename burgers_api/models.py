from django.db import models

# Create your models here.
class Ingredientes(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre


class Hamburguesa(models.Model):
  nombre = models.CharField(max_length=100)
  precio = models.IntegerField()
  descripcion = models.CharField(max_length=200)
  imagen = models.CharField(max_length=200)
  ingredientes = models.ManyToManyField(Ingredientes, blank=True)
  
  def __str__(self):
    return self.nombre


