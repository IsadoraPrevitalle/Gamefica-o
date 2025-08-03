from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("tarefas", views.tarefas, name = 'tarefas'),
    path("tarefas/<id_tarefa>/", views.tarefa, name = 'tarefa'),
]
