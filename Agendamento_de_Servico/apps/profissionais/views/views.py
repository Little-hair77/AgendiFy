from django.shortcuts import render, redirect, get_object_or_404
from ..models.models import Profissional
from ..forms import ProfissionalForm

def listar_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'listar.html', {'profissionais': profissionais})

def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profissionais:listar')
    else:
        form = ProfissionalForm()

    return render(request, 'cadastrar.html', {'form': form})

def editar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('profissionais:listar')
    else:
        form = ProfissionalForm(instance=profissional)
    
    return render(request, 'form.html', {
        'form': form,
        'profissional': profissional,
        'modo': 'editar'
    })

def deletar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        profissional.delete()
        return redirect('profissionais:listar')

    return render(request, 'form.html', {
        'profissional': profissional,
        'modo': 'deletar'
    })