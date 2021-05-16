# Create your models here.
from django.db import models
from graphviz import Digraph
import os, re
from django.conf import settings

class Automato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosDeAceitacao = models.CharField(max_length=100)
    dicionarioTransicao = models.CharField(max_length=1000)
    diagrama = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosDeAceitacao(self):
        return str(set(self.estadosDeAceitacao.split()))

    def dTransInTable(self):
        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        table = []
        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        table.append(linha)

        for estado in self.estados.split():
            linha =[estado]
            for simbolo in self.alfabeto.split():
                linha.append(dTrans[(estado, simbolo)])
            table.append(linha)
        return table

    def valida_sequencia(self, sequencia):

        estado = self.estadoInicial
        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                estado = dTrans[(estado, simbolo)]
            else:
                return False

        if estado in self.estadosDeAceitacao:
            return True
        else:
            return False

    def desenha_diagrama(self):

        d = Digraph(name=self.descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(self.estados.split()) - set(self.estadosDeAceitacao.split())
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in self.estadosDeAceitacao.split():
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', self.estadoInicial)

        for transicao_comma in self.dicionarioTransicao.split():
            transicao = transicao_comma.split('-')
            d.edge(transicao[0], transicao[2], label=transicao[1])

        d.format = 'svg'
        self.diagrama = f"computacao/images/afd/{str(self.nome).replace(' ', '_')}.svg"
        d.render(f"computacao/static/computacao/images/afd/{str(self.nome).replace(' ', '_')}")


class Maquina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosDeAceitacao = models.CharField(max_length=100)
    dicionarioTransicao = models.CharField(max_length=1000)
    diagrama = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosDeAceitacao(self):
        return str(set(self.estadosDeAceitacao.split()))

    def dTransInTable(self):
        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        table = []
        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        table.append(linha)

        temp = linha[1:]
        for estado in self.estados.split():
            linha=[estado]
            for simbolo in temp:
                encontra = False
                for dicEstado, dicSimbolo in dTrans:
                    if dicSimbolo[0] == simbolo and dicEstado == estado:
                        linha.append("(" + dicSimbolo[1] + "," + dicSimbolo[2] + "," + dTrans[(estado, dicSimbolo)] + ")")
                        encontra = True
                        break
                if encontra == False:
                    linha.append("")
            table.append(linha)
        return table

    def valida_sequencia(self, sequencia):
        estadoAtual = self.estadoInicial
        sequencia = '$' + sequencia + '$'

        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        fita = 1
        movimento = ''
        while True:
            if sequencia[fita] in self.alfabeto:
                for estado, simbolo in dTrans:
                    if estado == estadoAtual and sequencia[fita] == simbolo[0]:
                        if sequencia[fita] == '$':
                            if movimento == 'R':
                                sequencia = sequencia + '$'
                            elif movimento == 'L':
                                sequencia = '$' + sequencia
                            else:
                                sequencia = '$' + sequencia + '$'
                        sequencia = sequencia[:fita] + simbolo[1] + sequencia[fita + 1:]
                        if simbolo[2] == 'R':
                            fita += 1
                            movimento = 'R'
                            estadoAtual = dTrans[(estado, simbolo)]
                            break
                        elif simbolo[2] == 'L':
                            fita -= 1
                            movimento = 'L'
                            estadoAtual = dTrans[(estado, simbolo)]
                            break
                        else:
                            return False
                else:
                    break
            else:
                return False
        if estadoAtual in self.estadosDeAceitacao:
            self.sequenciaFinal = sequencia
            return True
        else:
            return False

    def desenha_diagrama(self):

        d = Digraph(name=self.descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(self.estados.split()) - set(self.estadosDeAceitacao.split())
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in self.estadosDeAceitacao.split():
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', self.estadoInicial)

        for transicao_comma in self.dicionarioTransicao.split():
            transicao = transicao_comma.split('-')
            d.edge(transicao[0], transicao[2], label=transicao[1])

        d.format = 'svg'
        self.diagrama = f"computacao/images/turing/{str(self.nome).replace(' ', '_')}.svg"
        d.render(f"computacao/static/computacao/images/turing/{str(self.nome).replace(' ', '_')}")


class Expressao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    regex = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printRegex(self):
        return self.regex

    def valida_sequencia(self, sequencia):
        regex = re.compile(self.regex)

        if re.match(regex, sequencia):
            return True
        else:
            return False
