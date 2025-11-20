from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from models.models import Empresa
from forms import EmpresaForm, EditarEmpresaForm

def listar_empresa(request):    
    empresas = Empresa.objects.all()
    return render(request, 'templates/listar.html', {'empresas':empresas})

def detalhar_empresa(request):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'templates/detalhes.html', {'empresa': empresa})

def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.proprietario = request.user
            empresa.save()
            return redirect('listar_empresas')
    else:
        form = EmpresaForm()
    
    return render(request, 'templates/cadastrar.html', {'form': form})

def editar_empresa(request):
    empresa = get_object_or_404()
    form = EditarEmpresaForm(request.POST or None, instance=empresa)
    if form.is_valid():
        form.save()
        return render('listar_empresas')
    
    return render(request, 'templates/editar.html', {'form':form, 'empresa':empresa})

def deletar_empresa(request):
    empresa = get_object_or_404()
    if request.method == 'POST':
        empresa.delete()
        return redirect('listar_empresas')
    
    return render(request, 'templates/deletar.html', {'empresa': empresa})
