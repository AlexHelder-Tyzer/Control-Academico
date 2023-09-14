from django.http import HttpResponse
from django.template import Template, Context, loader


# REQUEST -> Todas las peticiones que hace un usuario desde el navegador
# HTTPResponse -> Todas las respuestas mediante el protocolo HTTP

def inicio(request):
    return HttpResponse("Hola Mundo, esta es mi primera aplicacion.")

def estudiante(request):
    template = loader.get_template('estudiante.html') #registrar la direccion en settings
    document = template.render()
    return HttpResponse(document)

def curso(request):
    template = loader.get_template('curso.html') #registrar la direccion en settings
    document = template.render()
    return HttpResponse(document)


def saludo(request, nombre, edad):
    return HttpResponse(f"Me llamo {nombre} y tengo {edad} años, mucho gusto...")

def saludo2(request, nombre, edad):
    if str(edad).isnumeric():
        cadena = f"Me llamo {nombre} y tengo {edad} años, mucho gusto..."
    else:
        cadena = "El parametro edad no es número válido."
    return HttpResponse(cadena)

def saludo3(request, nombre):
    cadena = f"Me llamo {nombre}, mucho gusto..."
    return HttpResponse(cadena)

def html(request):
    frutas = ['Plátano', 'manzana', 'naranja', 'pera']
    # cadena = """
    #         <ul>
    #             <li>platano<li>
    #             <li>manzana<li>
    #             <li>naranja<li>
    #             <li>pera<li>
    #         </ul>
    #         """
    cadena = ''
    for data in frutas:
        cadena += f'<li>{data}</li>'
    cadena = f"<ul>{cadena}</ul>"
    return HttpResponse(cadena)

def html2(request):
    titulo = "Mi primera pagina con Django"
    alumnos = ['Eduardo Tolentino','Alberto Huamani','Alex Huancara','Rosa Milagro esta molestaaaa']
    alumno_curso = [
        {'nombre':'Eduardo Tolentino', 'cursos':'Matematica, Comunicacion', 'estado': '0'},
        {'nombre':'Alberto Huamani', 'cursos':'Matematica, Comunicacion', 'estado': '1'},
        {'nombre':'EAlex Huancara', 'cursos':'Administracion, Comunicacion', 'estado': '1'},
        {'nombre':'Juan Perez', 'cursos':'Fisica, Comunicacion', 'estado': '0'},

    ]
    
    context = {
        'list_alumno' : alumnos,
        'titulo' : titulo,
        'list_alumnocurso':alumno_curso,
    }
    template = loader.get_template('plantilla.html') #registrar la direccion en settings
    document = template.render(context)
    return HttpResponse(document)