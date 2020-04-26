from django.shortcuts import render

# Create your views here.
def listar_tarefas(request):
    nome_tarefa = "Assitir a semana Python e Django da TreinaWeb"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})