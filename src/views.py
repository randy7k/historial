from django.shortcuts import render, get_object_or_404, redirect
from src.models import Objetivo, Consecucion
from src.forms import ObjetivoForm, ConsecucionForm
from django.views.generic.edit import UpdateView,DeleteView


def index(request):
    objetivos = Objetivo.objects.all()
    consecuciones = Consecucion.objects.all()

    if request.method == 'POST':
        data = request.POST
        objetivo_form = ObjetivoForm(data)
        if objetivo_form.is_valid():
            objetivo_form.save()
        else:
            print(objetivo_form.erros)
    else:
        objetivo_form = ObjetivoForm()

    return render(request,'src/index.html', {
        'objetivos': objetivos,
        'objetivo_form': objetivo_form,
        'consecuciones': consecuciones,
    })

def objetivo(request, objetivo_id):
    objetivo = Objetivo.objects.get(id=objetivo_id)
    consecuciones = Consecucion.objects.filter(objetivo=objetivo)
    consecucion_form = ConsecucionForm()
    if request.method == 'POST':
        data = request.POST
        if data['_method'] == 'EditarObjetivo':
            objetivo_form = ObjetivoForm(data, instance=objetivo)
            if objetivo_form.is_valid():
                objetivo.save()
            else:
                print(objetivo_form.erros)
        else:
            objetivo_form = ObjetivoForm()

        if data['_method'] == 'EditarConsecucion':
            consecucion = get_object_or_404(Consecucion, id = data['consecucion_id'])
            consecucion_form = ConsecucionForm(data, instance=consecucion)
            tmp_consecucion_form = consecucion_form.data.copy()
            tmp_consecucion_form.setlist('objetivo', [str(objetivo.id)])
            consecucion_form.data = tmp_consecucion_form
            if consecucion_form.is_valid():
                consecucion.save()
            else:
                print(consecucion_form.errors)
            
        else:
            consecucion_form = ConsecucionForm()

        
        if data['_method'] == 'AgregarConsecucion':
            consecucion_form = ConsecucionForm(data)
            tmp_consecucion_form = consecucion_form.data.copy()
            tmp_consecucion_form.setlist('objetivo', [str(objetivo.id)])
            consecucion_form.data = tmp_consecucion_form
            if consecucion_form.is_valid():
                consecucion_form.save()
            else:
                print(consecucion_form.errors)
        else:
            consecucion_form = ConsecucionForm()

    else:
        objetivo_form = ObjetivoForm()
    return render(request,'src/objetivo.html', {
        'objetivo': objetivo,
        'consecuciones': consecuciones,
        'objetivo_form': objetivo_form,
        'consecucion_form': consecucion_form,
    })

def delete_objetivo(request, objetivo_id):
    objetivo = Objetivo.objects.get(id=objetivo_id)
    if objetivo:
        objetivo.delete()
    objetivos = Objetivo.objects.all()
    consecuciones = Consecucion.objects.all()
    return redirect('index')

def add_objetivo(request):
    if request.method == 'POST':
        data = request.POST
        objetivo_form = ObjetivoForm(data, instance=objetivo)
        if objetivo_form.is_valid():
            objetivo.save()
        else:
            print(objetivo_form.erros)
    else:
        objetivo_form = ObjetivoForm()
    return render(request,'src/objetivo.html', {
        'objetivo_form': objetivo_form,
    })