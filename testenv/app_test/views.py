from django.shortcuts import render, HttpResponse, redirect
from .models import Task

from secretary import Renderer

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/test')

def getTasks():
    tasks = Task.objects.all()
    return tasks

def viewsecretary(request):

    engine = Renderer()
    template = open('/home/sysadmin/Documents/test.ods', 'rb')
    #output = open('/home/sysadmin/Documents/test_output.ods', 'wb')
    #output.write(engine.render(template,  foo="Probando funcion"))
    print("**** Reporte renderizado correctamente ******")

    content_type= 'application/vnd.oasis.opendocument.text'
    tasks = Task.objects.all()
    with open('/home/sysadmin/Documents/test_output.ods', 'rb') as archivo_salida:
       # response = HttpResponse(archivo_salida.read(),

        #response = HttpResponse(engine.render(template,  foo="Probando funcion"),
        response = HttpResponse(engine.render(template,  tasks=getTasks()),
        content_type=content_type)
        response['Content-Disposition'] = 'inline; filename=pruebaODS.ods'
        return response

def viewsecretaryODT(request):

    engine = Renderer()
    template = open('/home/sysadmin/Documents/testods.odt', 'rb')
    #output = open('/home/sysadmin/Documents/test_output.ods', 'wb')
    #output.write(engine.render(template,  foo="Probando funcion"))
    print("**** Reporte renderizado correctamente ******")

    content_type= 'application/vnd.oasis.opendocument.text'
    tasks = Task.objects.all()
    with open('/home/sysadmin/Documents/test_output.ods', 'rb') as archivo_salida:
       # response = HttpResponse(archivo_salida.read(),

        #response = HttpResponse(engine.render(template,  foo="Probando funcion"),
        response = HttpResponse(engine.render(template,  tasks=getTasks()),
        content_type=content_type)
        response['Content-Disposition'] = 'inline; filename=pruebaODS.odt'
        return response


#exportar y descargar archivo

