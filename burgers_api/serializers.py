from rest_framework import serializers
from .models import Hamburguesa, Ingredientes

class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ('nombre', 'precio','descripcion','imagen','ingredientes')

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredientes
        fields = ('nombre', 'descripcion')