'''
    GRAFO DIRIGIDO
'''

from math import inf


class Arco:
    def __init__(self, u, v, peso):
        self.origem = u
        self.destino = v
        self.peso = peso


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo


class GrafoDirigido:
    def __init__(self):
        self.vertices = []
        self.arcos = []

    # Insere um vértice v já criado
    def inserirVertice(self, v):
        self.vertices.append(v)

    # Insere um arco de u para v
    def inserirArco(self, u, v, peso):
        self.arcos.append(Arco(u, v, peso))

    def obterArco(self, u, v):
        for arco in self.arcos:
            if arco.origem == u and arco.destino == v:
                return arco
        return False

    # Obtém vértice com indice i
    def obterVertice(self, i):
        for v in self.vertices:
            if int(v.indice) == int(i):
                return v
        return False

    # Retorna a quantidade de vértices
    def qtdVertices(self):
        return len(self.vertices)

    # Retorna a quantidade de arcos
    def qtdArcos(self):
        return len(self.arcos)

    # Retorna o grau do vértice v
    def grau(self, v):
        grau = 0
        for e in self.arcos:
            if v == e.origem or v == e.destino:
                grau += 1
        return grau

    # Retorna o rótulo do vértice v
    def rotulo(self, v):
        return v.rotulo

    # Retorna os vértices vizinhos de v
    def vizinhos(self, v):
        vizinhos = []
        for e in self.arcos:
            if v == e.origem:
                vizinhos.append(e.destino)
        return vizinhos

    # Retorna as arestas conectadas a v
    def arcosVizinhos(self, v):
        vizinhos = []
        for e in self.arcos:
            if v == e.origem:
                vizinhos.append(e)
        return vizinhos

    # Se existe arco entre u e v, retorna verdadeiro, senão, retorna falso
    def haArco(self, u, v):
        for e in self.arcos:
            if u == e.origem and v == e.destino:
                return True
        return False

    # Retorna o peso do arco (u, v), se não existir, retorna infinito positivo
    def peso(self, u, v):
        if u == v:
            return 0
        for e in self.arcos:
            if u == e.origem and v == e.destino:
                return e.peso
        return inf

    def ler(self, arquivo):
        arq = open(arquivo, "r")

        qtVertices = int(arq.readline()[10:])
        for i in range(qtVertices):
            linha = arq.readline()
            indice, rotulo = linha.split()
            indice = int(indice)
            rotulo = rotulo.replace('"', '')
            v = Vertice(int(indice), rotulo)
            self.inserirVertice(v)

        arq.readline()

        for linha in arq:
            u, v, peso = linha.split()
            self.inserirArco(self.obterVertice(u), self.obterVertice(v), float(peso))

        arq.close()
