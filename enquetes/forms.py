from django import forms
from .models import Questao, Alternativa

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['descricao']
        widgets = {
            'descricao': forms.TextInput(attrs={'class':'form-control','placeholder': 'Digite a pergunta...'}),
        }

class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = ['descricao']
        widgets = {
            'descricao': forms.TextInput(attrs={'class':    'form-control', 'placeholder': 'Digite a alternativa/opção de escolha....'}),
        }
