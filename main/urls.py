from django.urls import path
from main.views import TaskList
urlpatterns = [
    path('main', TaskList.as_view(), name='task_list')                                                                                
]
