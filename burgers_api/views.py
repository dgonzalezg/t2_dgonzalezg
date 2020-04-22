from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingredientes
from rest_framework.response import Response


# Create your views here.

class HamburguesaViewSet(viewsets.ModelViewSet):
     queryset = Hamburguesa.objects.all().order_by('nombre')
     serializer_class = HamburguesaSerializer

#     def list(self, request):
#         queryset = Hamburguesa.objects.all().order_by('nombre')
#         serializer = HamburguesaSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Hamburguesa.objects.all().order_by('nombre')
#         hamburguesa = get_object_or_404(queryset, pk=pk)
#         serializer = HamburguesaSerializer(hamburguesa)
#         return Response(serializer.data)
    
    

class IngredientesViewSet(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all().order_by('nombre')
    serializer_class = IngredienteSerializer

    