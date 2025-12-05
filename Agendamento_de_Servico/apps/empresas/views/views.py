from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Empresa
from ..forms import EmpresaForm, EditarEmpresaForm

def listar_empresas(request):    
    empresas = Empresa.objects.all()
    return render(request, 'listar_empresas.html', {'empresas':empresas})

def detalhes_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    return render(request, 'detalhes_empresa.html', {'empresa': empresa})

def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.dono = request.user   
            empresa.save()
            return redirect('listar_empresas')
    else:
        form = EmpresaForm()

    return render(request, 'cadastrar_empresa.html', {'form': form})

def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    form = EditarEmpresaForm(request.POST or None, instance=empresa)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_empresas')
    
    return render(request, 'editar.html', {
        'form': form,
        'empresa': empresa,
        'modo': 'editar'
    })

def deletar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST':
        empresa.delete()
        return redirect('listar_empresas')
    
    return render(request, 'deletar.html', {
        'empresa': empresa,
        'modo': 'deletar'
    })
