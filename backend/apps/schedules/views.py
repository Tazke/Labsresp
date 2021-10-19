from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.schedules.forms import FormPetition

# Create your views here.

def calendario(request):
    template_name="calendario.html"
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)

def reserva(request):
    template_name="reserva.html"
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)

def administrar(request):
    template_name="administrar.html"
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)

def salas(request):
    template_name="salas.html"
    petition_form = FormPetition()
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)

def formpetition(request):
    template_name="salas.html"
    petition_form = FormPetition()
    if petition_form.is_valid():
        petition_form.save()
        petition_form = FormPetition()
    return render(request, template_name, {"form":petition_form, "mensaje":'OK'})
