from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""ver como manejar esto del super usuario"""
# Creando un usuario administrador predeterminado
#class Administrador(models.Model):

   # if not User.objects.filter(username='admin').exists():
    #    User.objects.create_superuser('oscar@unah.hn', '1234abc')

class Autor(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion
    
class Autor(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion
        

class Editorial(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class GeneroLibro(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Idioma(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Libro(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    id_genero_libro = models.ForeignKey(GeneroLibro, on_delete=models.CASCADE)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    edicion = models.IntegerField()
    year_publicacion = models.IntegerField()
    fotolibro = models.ImageField(upload_to='fotos')
    resumen = models.TextField()

    def __str__(self):
        return self.titulo + " " + self.id_generolibro + " " + self.id_autor + " " + self.edicion + " " + self.fotolibro

class Ciudad(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_identidad = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    foto_usuario = models.ImageField(upload_to='fotos')

    def __str__(self):
        return self.email + " " + self.password
    



    