from django.contrib import admin
from .models import Estudiante
from .models import Curso, Matricula



# Register your models here.
# admin.site.register(Estudiante)
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'dni', 'nombre', 'apellido', 'estado'] #atributos que se muestran en la lista
    exclude = ['estado',] #exclusion de atributo para editar
    ordering = ['nombre', 'apellido'] #orden que muestra
    search_fields = ['dni', 'nombre', 'apellido'] #criterio de busqueda

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'estado'] #atributos que se muestran en la lista
    # exclude = ['estado',] #exclusion de atributo para editar
    # ordering = ['nombre', 'apellido'] #orden que muestra
    # search_fields = ['dni', 'nombre', 'apellido'] #criterio de busqueda

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_estudiante', 'nombre_curso', 'estado'] #atributos que se muestran en la lista

    def nombre_estudiante(self, obj):
        return obj.estudiante.nombre
    
    def nombre_curso(self, obj):
        return obj.curso.nombre