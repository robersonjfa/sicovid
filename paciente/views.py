from django.shortcuts import render, redirect
from .forms import PacienteForm
from monitor.models import Paciente

# Create your views here.
def paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('paciente/show')
            except Exception as e:
                print(e)
                pass
    else:
        form = PacienteForm()
    return render(request, 'paciente/index.html', {'form': form})

def show(request):
    pacientes = Paciente.objects.all()
    return render(request, "paciente/show.html", {'pacientes': pacientes})

def edit(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    return render(request, 'paciente/edit.html', {'paciente': paciente})

def update(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    form = PacienteForm(request.POST, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect("/paciente/show")
    return render(request, 'paciente/edit.html', {'paciente': paciente})

def destroy(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    paciente.delete()
    return redirect("/paciente/show")