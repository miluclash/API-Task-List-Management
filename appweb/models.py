from django.db import models

# AQUI VAN LOS MODELOS (CLASES) DE LA APP

class ListaTareas(models.Model):
    #No añado el id como primary key, ya que django ya me crea uno automaticamnete --> id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.name #Devuelve el nombre de la lista toString()


class Tarea(models.Model):
    #id generado por django
    title = models.CharField(max_length=50) #Descripcion de la tarea
    completed = models.BooleanField(default=False) #Indica si la tarea esta completada o no
    created_at = models.DateField(auto_now_add=True) #Fecha creacion
    task_list = models.ForeignKey(ListaTareas,on_delete=models.CASCADE, related_name='tareas')
    
    def __str__(self):
        return self.title # devuelve el titulo de la tarea

