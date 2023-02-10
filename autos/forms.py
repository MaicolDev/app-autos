from django.forms import ModelForm
from .models import Auto


class FormularioAuto(ModelForm):
    class Meta:
        model = Auto
        fields = ['marca','modelo','descripcion', 'año','precio','vendido']
