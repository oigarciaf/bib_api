from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Libro, Autor, Editorial, GeneroLibro, Idioma, Ciudad, Usuario
from .serializers import LibroSerializer, AutorSerializer, EditorialSerializer, GeneroLibroSerializer, IdiomaSerializer, CiudadSerializer, UsuarioSerializer

# Vistas para el modelo Autor
@api_view(['GET', 'POST'])
def autor_list(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AutorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AutorSerializer(autor, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=204)


# Vistas para el modelo Editorial
@api_view(['GET', 'POST'])
def editorial_list(request):
    if request.method == 'GET':
        editoriales = Editorial.objects.all()
        serializer = EditorialSerializer(editoriales, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EditorialSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def editorial_detail(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)

    if request.method == 'GET':
        serializer = EditorialSerializer(editorial)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EditorialSerializer(editorial, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        editorial.delete()
        return Response(status=204)


# Vistas para el modelo GeneroLibro
@api_view(['GET', 'POST'])
def genero_libro_list(request):
    if request.method == 'GET':
        generos = GeneroLibro.objects.all()
        serializer = GeneroLibroSerializer(generos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GeneroLibroSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
