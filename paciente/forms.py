from django import forms
from monitor.models import Paciente
from django.forms.widgets import NumberInput

SEXOS = (
    ('F', "Feminino"),
    ('M', 'Masculino')
)

# creating a form
class PacienteForm(forms.ModelForm):
    sexo = forms.ChoiceField(widget=forms.RadioSelect(), choices=SEXOS)
    datanascimento = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    # create meta class
    class Meta:
        # specify model to be used
        model = Paciente

        # specify fields to be used
        fields = [
            "cpf",
            "nome",
            "datanascimento",
            "sexo"
        ]