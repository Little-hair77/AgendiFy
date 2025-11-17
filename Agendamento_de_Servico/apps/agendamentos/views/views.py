from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Agendamento
from forms import AgendamentoForm

# Create your views here.

