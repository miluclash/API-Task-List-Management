from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ListaTareas,Tarea
from .serializers import ListaTareasSerializer,TareaSerializer

@api_view(['GET', 'POST'])
def gestionar_listas(request):
    # GET: Devolver todas las listas
    if request.method == 'GET':
        instancias = ListaTareas.objects.all()
        traductor = ListaTareasSerializer(instancias, many=True)
        return Response(traductor.data)

    # POST: Crear una lista nueva
    elif request.method == 'POST':
        traductor = ListaTareasSerializer(data=request.data)
        if traductor.is_valid():
            traductor.save()
            return Response(traductor.data, status=status.HTTP_201_CREATED)
        return Response(traductor.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def detalle_lista(request, pk):
    # Buscamos la lista por su ID (pk)
    lista = get_object_or_404(ListaTareas, pk=pk)

    if request.method == 'GET':
        serializer = ListaTareasSerializer(lista)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        lista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def gestionar_tareas(request, pk):
    # Buscamos la lista para saber a qué tareas nos referimos
    lista = get_object_or_404(ListaTareas, pk=pk)

    if request.method == 'GET':
        tareas = Tarea.objects.filter(task_list=lista)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Al crear la tarea, le pasamos el ID de la lista automáticamente
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_list=lista)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE','GET'])
def detalle_tarea(request, list_id, task_id):
    # Buscamos la tarea que pertenezca a esa lista específica
    tarea = get_object_or_404(Tarea, id=task_id, task_list_id=list_id)

    if request.method == 'PATCH':
        # 'partial=True' permite actualizar solo el campo 'completed'
        serializer = TareaSerializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data)

#Metodo para la interfaz web
#**ACTUALIZACION**
#Ahora se pueden visualizar las tareas, ademas de comprobar, leer y eliminarlas

def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # Caso 1: Crear una nueva lista
        if action == 'crear_lista':
            nombre = request.POST.get('nombre_lista')
            if nombre:
                ListaTareas.objects.create(name=nombre)
        
        # Caso 2: Añadir tarea a una lista específica
        elif action == 'añadir_tarea':
            list_id = request.POST.get('list_id')
            titulo = request.POST.get('titulo_tarea')
            lista = get_object_or_404(ListaTareas, id=list_id)
            Tarea.objects.create(title=titulo, task_list=lista)

        # Caso 3: Cambiar estado (Completar/Pendiente)
        elif action == 'toggle_tarea':
            tarea_id = request.POST.get('tarea_id')
            tarea = get_object_or_404(Tarea, id=tarea_id)
            tarea.completed = not tarea.completed # Invierte el estado
            tarea.save()

        # Caso 4: Borrar tarea
        elif action == 'borrar_tarea':
            tarea_id = request.POST.get('tarea_id')
            get_object_or_404(Tarea, id=tarea_id).delete()

        #Caso 5: Borrar lista
        elif action == 'borrar_lista':
            list_id = request.POST.get('list_id')
            get_object_or_404(ListaTareas, id=list_id).delete()
        return redirect('home')

    listas = ListaTareas.objects.all().prefetch_related('tareas')
    return render(request, 'appweb/index.html', {'listas': listas})