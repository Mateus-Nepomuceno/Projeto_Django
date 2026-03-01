from django.urls import path
from enquetes import views

app_name = "enquetes"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('<int:questao_id>/voto/', views.voto, name='voto'),
    path('nova/', views.nova_enquete, name='nova_enquete'),
    path('<int:questao_id>/nova_alternativa/', views.nova_alternativa, name='nova_alternativa'),
    path('alternativa/<int:alternativa_id>/excluir/', views.excluir_alternativa, name='excluir_alternativa'),
    path('alternativa/<int:alternativa_id>/editar/', views.editar_alternativa, name='editar_alternativa'),
]