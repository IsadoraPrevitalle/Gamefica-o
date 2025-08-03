from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarefa

def index(request):
    """Página principal da aplicação"""
    return render(request, 'games/index.html')

@login_required
def tarefas(request):
    """Página que exibe todas as tarefas por usuários"""
    tarefas = Tarefa.objects.all()
    context = {'tarefas': tarefas}
    return render(request, 'games/tarefas.html', context)

@login_required
def tarefa(request, id_tarefa):
    """Exibe uma unica tarefa e seus atributos"""
    tarefa = Tarefa.objects.get(id = id_tarefa)
    context = {'tarefa': tarefa}
    return render(request, 'games/tarefa.html', context)