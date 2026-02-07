#AQUI ESTABLECEMOS COMO TRANSFORMAR LOS MODELOS A JSON
from rest_framework import serializers
from .models import Tarea, ListaTareas

#Serializador para las Tareas
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'title', 'completed', 'created_at', 'task_list']
        read_only_fields = ['task_list']

#Serializador para las Listas de Tareas
class ListaTareasSerializer(serializers.ModelSerializer):
    tasks = TareaSerializer(many=True, read_only=True)

    class Meta:
        model = ListaTareas
        fields = ['id', 'name', 'created_at', 'tasks']