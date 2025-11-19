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