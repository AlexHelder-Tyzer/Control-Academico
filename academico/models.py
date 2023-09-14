from django.db import models

# Create your models here.

LISTA_ESTADO = (
        ('0','Deshabilitado'),
        ('1', 'Habilitado'),
    )

class Estudiante(models.Model):
    
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=LISTA_ESTADO)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=1, choices=LISTA_ESTADO)

# crear tablas con claves foraneas
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=LISTA_ESTADO)

    class Meta: #limita valores unicos, si se ingresa valores repetidos no se permite
        unique_together = (('estudiante', 'curso'),)
