from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingredientes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
@api_view(['GET','POST'])
def burgers_list(request):
     if request.method == 'GET':
          burgers = Hamburguesa.objects.all()
          serializer = HamburguesaSerializer(burgers, many=True,context={'request': request})
          return Response(serializer.data,status=status.HTTP_200_OK)
     elif request.method == 'POST':
          if 'id' in request.data.keys() or 'ingredientes' in request.data.keys():
               return Response(status=status.HTTP_400_BAD_REQUEST)
          serializer = HamburguesaSerializer(data=request.data,context={'request': request})
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def burger_detail(request, pk):
          
     try:
          pk = int(pk)
          burger = Hamburguesa.objects.get(pk=pk)
     except ValueError:
          return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
     except Hamburguesa.DoesNotExist:
          return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
          serializer = HamburguesaSerializer(burger,context={'request': request})
          return Response(serializer.data)
     if request.method == 'PATCH':
          if 'id' in request.data.keys() or 'ingredientes' in request.data.keys():
               return Response(status=status.HTTP_400_BAD_REQUEST)
          serializer = HamburguesaSerializer(burger,data=request.data, context={'request': request})
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     if request.method == 'DELETE':
          burger.delete()
          return Response(status=status.HTTP_200_OK)
     
@api_view(['PUT','DELETE'])
def burguer_update(request,burguer_id,ingredient_id):
     try:
          burger = Hamburguesa.objects.get(pk=burguer_id)
          ingredient = Ingredientes.objects.get(pk=ingredient_id)
     except Hamburguesa.DoesNotExist:
          return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
     except Ingredientes.DoesNotExist:
          return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'PUT':
          burger.ingredientes.add(ingredient)
          return HttpResponse(status=status.HTTP_201_CREATED)
     if request.method == 'DELETE':
          try: 
               burger.ingredientes.get(pk=ingredient.id) 
               burger.ingredientes.remove(ingredient)
               return HttpResponse(status=status.HTTP_200_OK)
          except:
               return HttpResponse(status=status.HTTP_404_NOT_FOUND)  

@api_view(['GET','POST'])
def ingredients_list(request):
     if request.method == 'GET':
          ingredients = Ingredientes.objects.all()
          serializer = IngredienteSerializer(ingredients, many=True)
          return Response(serializer.data)
     elif request.method == 'POST':
          if 'id' in request.data.keys():
               return Response(status=status.HTTP_400_BAD_REQUEST)
          serializer = IngredienteSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def ingredient_detail(request, pk):
     try:
          pk = int(pk)
          ingredient = Ingredientes.objects.get(pk=pk)
     except Ingredientes.DoesNotExist:
          return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     except ValueError:
          return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
     if request.method == 'GET':
          serializer = IngredienteSerializer(ingredient)
          return Response(serializer.data)
     elif request.method == 'DELETE':
          flag = False
          for hamburguesa in Hamburguesa.objects.all():
               try:
                    hamburguesa.ingredientes.get(pk=ingredient.id)
                    flag = True
               except:
                    pass
          if flag:
               return HttpResponse(status=status.HTTP_409_CONFLICT)
          ingredient.delete()
          return HttpResponse(status=status.HTTP_200_OK)


    