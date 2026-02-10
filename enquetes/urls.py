from django.urls import path
from enquetes import views

app_name = "enquetes"
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /enquetes/5/
    path("<int:questao_id>/", views.detalhe, name="detalhe"),
    # ex: /enquetes/5/voto/
    path("<int:questao_id>/voto/", views.voto, name="voto"),
    # ex: /enquetes/5/resultados/
    path("<int:questao_id>/resultados/", views.resultados, name="resultados"),
]