from django import forms
from django.forms import ModelForm
from .models import Automato, Maquina, Expressao

class SequenciaForm(forms.Form):
    sequencia = forms.CharField(label='',
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Insira uma sequência',
                                    'size': '25'
                                }))


class AutomatoForm(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'   # pode-se especificar lista dos campos q queremos. podemos querer tudo excluindo alguns
        exclude = ['diagrama']

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'AFD que aceita sequências ...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosDeAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicionarioTransicao': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome do autómato',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        placeholders = {
            'nome': 'Nome do autómato',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique o AFD',
            'descricao': 'Descreva o tipo de sequências que o autómato reconhece',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (e.g. "0 1")',
            'estados': 'Insira os nomes dos estados separados por espaços (e.g. "A B")',
            'estadosDeAceitacao': 'Insira os estados separados por espaços (e.g. "A B")',
            'dicionarioTransicao': 'Insira as transicoes estadoInicial-simbolo-estadoSeguinte (e.g. "A-0-B A-1-A")'
        }


class MaquinaForm(ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'
        exclude = ['diagrama']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Máquina de Turing que aceita sequências ...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosDeAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicionarioTransicao': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome da Máquina de Turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        placeholders = {
            'nome': 'Nome da Máquina de Turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosDeAceitacao': 'Estado de aceitação',
            'dicionarioTransicao': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique a Máquina de Turing',
            'descricao': 'Descreva o tipo de sequências que a Máquina de Turing reconhece',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (e.g. "0 1")',
            'estados': 'Insira os nomes dos estados separados por espaços (e.g. "A B")',
            'estadosDeAceitacao': 'Insira os estados separados por espaços (e.g. "A B")',
            'dicionarioTransicao': 'Insira as transicoes estadoInicial-simbolo-estadoSeguinte (e.g. "A-0-B A-1-A")'
        }


class ExpressaoForm(ModelForm):
    class Meta:
        model = Expressao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Expressão Regular que aceita sequências ...'}),
            'regex': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome da Expressão Regular',
            'descricao': 'Descrição',
            'regex': 'Linguagem Regex'
        }

        placeholders = {
            'nome': 'Nome da Expressão Regular',
            'descricao': 'Descrição',
            'regex': 'Linguagem Regex'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique a Expressão Regular',
            'descricao': 'Descreva o tipo de sequências que a Expressão Regular reconhece',
            'regex': 'Insira uma linguagem Regex (e.g. "^[2789](.?[\d]{8}$")'
        }
