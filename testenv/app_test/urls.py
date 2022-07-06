from django.urls import path
from .views import viewsecretary, list_tasks, create_task,viewsecretaryODT

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name="create_task"),
    path('ods', viewsecretary),
    path('odt', viewsecretaryODT)
]

