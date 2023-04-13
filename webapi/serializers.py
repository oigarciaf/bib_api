from rest_framework import serializers
from .models import Libro, Autor, Editorial, GeneroLibro, Idioma, Ciudad, Usuario

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'descripcion')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('id', 'descripcion')

class GeneroLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLibro
        fields = ('id', 'descripcion')

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id', 'descripcion')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id','id_autor',
                   'id_editorial','id_genero_libro',
                   'id_idioma','titulo',
                   'edicion','year_publicacion',
                   'fotolibro','resumen'
                  )


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id','descripcion')



class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id,','id_ciudad',
                   'nombre','apellido',
                   'numero_identidad',
                   'email', 'password', 
                   'telefono', 'foto_usuario'
                  )