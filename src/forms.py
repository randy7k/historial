# socio/forms.py
from django import forms
from src.models import Objetivo, Consecucion

class ObjetivoForm(forms.ModelForm):
    class Meta():
        model = Objetivo
        fields = (
            'metrica',
            'descripcion',
        )

class ConsecucionForm(forms.ModelForm):
    class Meta():
        model = Consecucion
        fields = (
            'objetivo',
            'descripcion',
            'meta',
            'porcentaje_de_consecucion',
        )
