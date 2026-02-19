from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import Questao, Alternativa
from .forms import QuestaoForm, AlternativaForm

# Create your views here.

def index(request):
    lista_questoes_recentes = Questao.objects.order_by("-data_pub")[:5]
    contexto = {"lista_questoes_recentes":lista_questoes_recentes}
    return render(request, 'enquetes/index.html', contexto)

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    form_alternativa = AlternativaForm()
    context = {
        'questao': questao,
        'form_alternativa': form_alternativa
    }
    return render(request, "enquetes/detalhe.html", context)

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

def nova_enquete(request):
    if request.method == "POST":
        try:
            form = QuestaoForm(request.POST)
            if form.is_valid():
                questao = form.save(commit=False)
                questao.data_pub = timezone.now()
                questao.save()
                return redirect('enquetes:index')
        except Exception as e:
            form.add_error(None,f"Ocorreu um erro inesperado ao criar enquete. {e}")
    else:
        form = QuestaoForm()

    return render(request, 'enquetes/cadastro.html', {'form': form})

def nova_alternativa(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)

    if request.method == "POST":
        try:
            form = AlternativaForm(request.POST)
            if form.is_valid():
                alternativa = form.save(commit=False)
                alternativa.questao = questao
                alternativa.save()
        except Exception as e:
            form.add_error(None, f"Ocorreu um erro inesperado. {e}")

    return redirect('enquetes:detalhe', questao_id=questao.id)