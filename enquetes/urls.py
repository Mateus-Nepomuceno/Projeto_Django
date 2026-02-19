from django.urls import path
from enquetes import views

app_name = "enquetes"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('<int:questao_id>/voto/', views.voto, name='voto'),
]