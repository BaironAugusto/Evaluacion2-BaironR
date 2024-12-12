from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm


def home(request):
    tareas = Tarea.objects.all()  
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = TareaForm()

    return render(request, 'home.html', {'tareas': tareas, 'form': form})


def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()  
    return redirect('home')  

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'editar_tarea.html', {'form': form, 'tarea': tarea})


