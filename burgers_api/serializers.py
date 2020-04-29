from rest_framework import serializers
from .models import Hamburguesa, Ingredientes


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = ['id','nombre', 'descripcion']


class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ingredient_detail'
    )
    class Meta:
        model = Hamburguesa
        fields = ['id','nombre', 'precio','descripcion','imagen','ingredientes']
