from django.shortcuts import render
from src.models import Objetivo, Consecucion

def index(request):
    objetivos = Objetivo.objects.all()
    consecuciones = Consecucion.objects.all()
    return render(request,'src/index.html', {
        'objetivos': objetivos,
        'consecuciones': consecuciones,
    })
    