from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Questao

# Create your views here.

def index(request):
    lista_questoes_recentes = Questao.objects.order_by("-data_pub")[:5]
    contexto = {"lista_questoes_recentes":lista_questoes_recentes}
    return render(request, 'enquetes/index.html', contexto)

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, "enquetes/detalhe.html", {"questao": questao})

def voto(request, questao_id) :
    return HttpResponse(f"Você está votando na Pergunta {questao_id}")

def resultados(request, questao_id) :
    response = f"Você está vendos os resultados da Pergunta {questao_id}"
    return HttpResponse(response)