from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Automato, Maquina, Expressao
from .forms import SequenciaForm, AutomatoForm, MaquinaForm, ExpressaoForm


def index(request):
    return render(request, 'computacao/index.html')


def automato(request, automato_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).valida_sequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/automato.html', context)


def automatos(request):

    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)


def novo_automato(request):

    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        new_automata = form.save()
        new_automata.desenha_diagrama()
        new_automata.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    context = {'form': form}

    return render(request, 'computacao/novo_automato.html', context)


def edita_automato(request, automato_id):

    instance = Automato.objects.get(id=automato_id)
    form = AutomatoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    context = {'form': form, 'automato_id':automato_id}
    return render(request, 'computacao/edita_automato.html', context)


def apaga_automato(request, automato_id):
    Automato.objects.filter(id=automato_id).delete()
    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)


def maquina(request, maquina_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Maquina.objects.get(id=maquina_id).valida_sequencia(sequencia)

    context = {
        'maquina': Maquina.objects.get(id=maquina_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/maquina.html', context)


def maquinas(request):

    context = {'maquinas': Maquina.objects.all()}
    return render(request, 'computacao/maquinas.html', context)


def nova_maquina(request):

    form = MaquinaForm(request.POST or None)
    if form.is_valid():
        nova_maquina = form.save()
        nova_maquina.desenha_diagrama()
        nova_maquina.save()
        return HttpResponseRedirect(reverse('computacao:maquinas'))

    context = {'form': form}
    return render(request, 'computacao/nova_maquina.html', context)


def edita_maquina(request, maquina_id):

    instance = Maquina.objects.get(id=maquina_id)
    form = MaquinaForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:maquinas'))

    context = {'form': form, 'maquina_id':maquina_id}
    return render(request, 'computacao/edita_maquina.html', context)


def apaga_maquina(request, maquina_id):
    Maquina.objects.filter(id=maquina_id).delete()
    context = {'maquinas': Maquina.objects.all()}
    return render(request, 'computacao/maquinas.html', context)


def expressao(request, expressao_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Expressao.objects.get(id=expressao_id).valida_sequencia(sequencia)

    context = {
        'expressao': Expressao.objects.get(id=expressao_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/expressao.html', context)


def expressoes(request):

    context = {'expressoes': Expressao.objects.all()}
    return render(request, 'computacao/expressoes.html', context)


def nova_expressao(request):

    form = ExpressaoForm(request.POST or None)
    if form.is_valid():
        nova_expressao = form.save()
        nova_expressao.save()
        return HttpResponseRedirect(reverse('computacao:expressoes'))

    context = {'form': form}
    return render(request, 'computacao/nova_expressao.html', context)


def edita_expressao(request, expressao_id):

    instance = Expressao.objects.get(id=expressao_id)
    form = ExpressaoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.save()
        return HttpResponseRedirect(reverse('computacao:expressoes'))

    context = {'form': form, 'expressao_id':expressao_id}
    return render(request, 'computacao/edita_expressao.html', context)


def apaga_expressao(request, expressao_id):
    Expressao.objects.filter(id=expressao_id).delete()
    context = {'expressoes': Expressao.objects.all()}
    return render(request, 'computacao/expressoes.html', context)
