from django.shortcuts import render, redirect
from .forms import EmpleadoForm, ProyectoForm, TareaForm
from .models import Empleado, Proyecto, Tarea

def formulario_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'formulario_empleado.html', {'form': form})

def formulario_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProyectoForm()
    return render(request, 'formulario_proyecto.html', {'form': form})

def formulario_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = TareaForm()
    return render(request, 'formulario_tarea.html', {'form': form})

def inicio(request):
    # Obtener datos de empleados, proyectos o tareas si es necesario
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    tareas = Tarea.objects.all()
    return render(request, 'inicio.html', {'empleados': empleados, 'proyectos': proyectos, 'tareas': tareas})
