'''
    GRAFO NÃO DIRIGIDO
'''

from math import inf


class Aresta:
    def __init__(self, u, v, peso):
        self.vertices = [u, v]
        self.peso = peso


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo


class GrafoNaoDirigido:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    # Insere um vértice v já criado
    def inserirVertice(self, v):
        self.vertices.append(v)

    # Insere uma aresta entre os vértices u e v
    def inserirAresta(self, u, v, peso):
        self.arestas.append(Aresta(u, v, peso))

    # Obtém vértice com indice i
    def obterVertice(self, i):
        for v in self.vertices:
            if int(v.indice) == int(i):
                return v
        return False

    # Retorna a quantidade de vértices
    def qtdVertices(self):
        return len(self.vertices)

    # Retorna a quantidade de arestas
    def qtdArestas(self):
        return len(self.arestas)

    # Retorna o grau do vértice v
    def grau(self, v):
        grau = 0
        for e in self.arestas:
            if v in e.vertices:
                grau += 1
        return grau

    # Retorna o rótulo do vértice v
    def rotulo(self, v):
        return v.rotulo

    # Retorna os vértices vizinhos de v
    def vizinhos(self, v):
        vizinhos = []
        for e in self.arestas:
            if v in e.vertices:
                if v == e.vertices[0]:
                    vizinhos.append(e.vertices[1])
                else:
                    vizinhos.append(e.vertices[0])
        return vizinhos

    # Retorna as arestas conectadas a v
    def arestasVizinhos(self, v):
        vizinhos = []
        for e in self.arestas:
            if v in e.vertices:
                vizinhos.append(e)
        return vizinhos

    # Se existe aresta entre u e v, retorna verdadeiro, senão, retorna falso
    def haAresta(self, u, v):
        for e in self.arestas:
            if u in e.vertices and v in e.vertices:
                return True
        return False

    # Retorna o peso da aresta {u, v}, se não existir, retorna infinito positivo
    def peso(self, u, v):
        if u == v:
            return 0
        for e in self.arestas:
            if u in e.vertices and v in e.vertices:
                return e.peso
        return inf

    # Carrega um grafo a partir de um arquivo
    def ler(self, arquivo):
        arq = open(arquivo, "r")

        qtVertices = int(arq.readline()[10:])
        for i in range(qtVertices):
            linha = arq.readline()
            indice = int(linha.split('"')[0])
            rotulo = linha.split('"')[1]
            v = Vertice(int(indice), rotulo)
            self.inserirVertice(v)

        arq.readline()

        for linha in arq:
            u, v, peso = linha.split()
            self.inserirAresta(self.obterVertice(u), self.obterVertice(v), float(peso))

        arq.close()
