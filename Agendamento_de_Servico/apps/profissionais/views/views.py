from django.shortcuts import render, redirect, get_object_or_404
from ..models import Profissional        
from ..forms import ProfissionalForm


def listar_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'listar_profissionais.html', {'profissionais': profissionais})


def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm()

    return render(request, 'cadastrar_profissional.html', {
        'form': form,
        'modo': 'cadastrar'
    })


def editar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm(instance=profissional)
    
    return render(request, 'cadastrar_profissional.html', {
        'form': form,
        'profissional': profissional,
        'modo': 'editar'
    })


def deletar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        profissional.delete()
        return redirect('listar_profissionais')

    return render(request, 'perfil_profissional.html', {
        'profissional': profissional,
        'modo': 'deletar'
    })

def detalhes_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    return render(request, 'perfil_profissional.html', {
        'profissional': profissional,
        'modo': 'detalhes'
    })