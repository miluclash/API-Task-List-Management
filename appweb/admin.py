from django.contrib import admin
from .models import ListaTareas, Tarea

# Register your models here.
admin.site.register(ListaTareas)
admin.site.register(Tarea)
#Para ver los modelos en /admin