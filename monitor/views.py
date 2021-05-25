from django.shortcuts import render
from .models import Sintoma, Paciente


def home(request):
    return render(request, 'index.html')


def buscar(request):
    try:
        paciente = Paciente.objects.get(cpf=request.POST['cpf'])
    except Paciente.DoesNotExist:
        paciente = None
    sintomas = Sintoma.objects.all()
    return render(request, 'paciente.html', {'sintomas': sintomas, 'cpf': request.POST['cpf'], 'paciente': paciente})


def testar(request):
    paciente = Paciente()
    paciente.cpf = request.POST['cpf']
    paciente.nome = request.POST['nome']
    paciente.datanascimento = request.POST['datanascimento']
    paciente.sexo = request.POST['sexo']
    paciente.latitude = request.POST['latitude']
    paciente.longitude = request.POST['longitude']
    paciente.resultado = sum(list(map(float, request.POST.getlist('sintomas'))))

    paciente.save()
    return render(request, 'resultado.html', {'paciente': paciente})
