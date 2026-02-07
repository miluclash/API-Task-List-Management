from django.urls import path
from . import views

urlpatterns = [
    path('listas/', views.gestionar_listas, name='gestionar_listas'),
    path('listas/<int:pk>/', views.detalle_lista), # Para borrar o ver una lista
    path('listas/<int:pk>/tareas/', views.gestionar_tareas), # Para ver/crear tareas de esa lista
    path('listas/<int:list_id>/tareas/<int:task_id>/', views.detalle_tarea),#Ruta para tareas individuales
    path('', views.home, name='home'), # Pagina principal 
    path('listas/', views.gestionar_listas),
]