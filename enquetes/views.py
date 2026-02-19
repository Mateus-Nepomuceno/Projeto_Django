from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Questao, Alternativa

# Create your views here.

def index(request):
    lista_questoes_recentes = Questao.objects.order_by("-data_pub")[:5]
    contexto = {"lista_questoes_recentes":lista_questoes_recentes}
    return render(request, 'enquetes/index.html', contexto)

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, "enquetes/detalhe.html", {"questao": questao})

def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        selecionada = questao.alternativa_set.get(pk=request.POST['alternativa'])
    except (KeyError, Alternativa.DoesNotExist):
        return render(
            request, 'enquetes/detalhes.html', {
            'questao': questao,
            'error_message': "Você não selecionou uma opção válida.",
        })
    else:
        selecionada.votos = F('votos') + 1
        selecionada.save()
    
        return HttpResponseRedirect(reverse('enquetes:resultados', args=(questao.id,)))

def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request, 'enquetes/resultados.html', {'questao': questao})