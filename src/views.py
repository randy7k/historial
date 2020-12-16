from django.shortcuts import render, get_object_or_404, redirect
from src.models import Objetivo, Consecucion
from src.forms import ObjetivoForm, ConsecucionForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View

class ObjetivoCreateView(CreateView):
    model = Objetivo    
    template_name = 'src/index.html'
    context = {}

    def get(self, request):
        self.context['objetivos'] = self.model.objects.all()
        return render(request, self.template_name, self.context)

    def post(self, request):
        objetivo_form = ObjetivoForm(request.POST)
        if objetivo_form.is_valid():
            objetivo_form.save()
        else:
            print(objetivo_form.erros)
        self.context['objetivos'] = self.model.objects.all()
        return render(request, self.template_name, self.context)

class ObjetivoUpdateView(UpdateView):
    model = Objetivo
    template_name = "src/consecucion.html"
    context = {}
    
    def get(self, request, *args, **kwargs):
        self.context['objetivo'] = self.model.objects.get(id=kwargs['objetivo_id'])
        self.context['objetivo_form'] = ObjetivoForm()
        self.context['consecuciones'] = Consecucion.objects.filter(objetivo=self.context['objetivo'])
        self.context['consecucion_form'] = ConsecucionForm()
        self.context['resultado'] = ''
        self.context['percentage'] = ''
        return render(request,'src/consecucion.html', self.context)
    
    def post(self, request, *args, **kwargs):
        objetivo = self.model.objects.get(id=kwargs['objetivo_id'])
        objetivo_form = ObjetivoForm()
        consecuciones = Consecucion.objects.filter(objetivo=objetivo)
        consecucion_form = ConsecucionForm()

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

        if data['_method'] == 'CalcularConsecucion':
            resultado = data['resultado']
            self.context['resultado'] = resultado
            self.context['percentage'] = calc_consecution_percentage(resultado, consecuciones)

        self.context['objetivo'] = objetivo
        self.context['objetivo_form'] = objetivo_form
        self.context['consecuciones'] = consecuciones
        self.context['consecucion_form'] = consecucion_form
        return render(request, self.template_name, self.context)

class ObjetivoDeleteView(DeleteView):
    model = Objetivo
    success_url ="/"

def is_asc(consecuciones):
    is_asc = True
    last = None
    for consecucion in consecuciones:
        if last == None:
            last = consecucion.meta
        else:
            if consecucion.meta < last:
                is_asc = False
    return is_asc

def calc_consecution_percentage(resultado, consecuciones):
    output = None
    if is_asc(consecuciones):
        for consecucion in consecuciones:
            if output == None:
                output = consecucion.porcentaje_de_consecucion
            if float(resultado) >= float(consecucion.meta):
                output = consecucion.porcentaje_de_consecucion
    else:
        for consecucion in consecuciones:
            if output == None:
                output = consecucion.porcentaje_de_consecucion
            if float(resultado) <= float(consecucion.meta):
                output = consecucion.porcentaje_de_consecucion
    return output
