from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    
class TaskList(ListView):
    model = Task 
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'
    

def task_list(request):
    tarefas = Task.objects.all() 
    context = {
        'tarefas':tarefas,
        'titulo_pagina': 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)

def task_concluido(request):
    a = 4
    b = 5
    c = a + b

    tarefas = Task.objects.filter(concluida=1   ) 
    context = {
        'tarefas':tarefas,
        'titulo_pagina':'Minhas Tarefas Concluidas'

    }
    return render(request, 'tasks/concluido.html', context)


def teste(request):

    tarefas = Task.objects.filter(concluida=1) 
    context = {
        'tarefas':tarefas,
        'titulo_pagina': 'Teste'

    }
    return render(request, 'tasks/aaaa.html', context)