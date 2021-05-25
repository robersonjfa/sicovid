from django.db import models


# Create your models here.
class Sintoma(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False, unique=True)
    percentual = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nome + ' - ' + self.percentual.__str__()


class Paciente(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False, null=False)
    datanascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=20, null=False)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    resultado = models.DecimalField(max_digits=6, decimal_places=2)
