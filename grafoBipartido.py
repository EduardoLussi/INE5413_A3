'''
    GRAFO BIPARTIDO
'''


class Aresta:
    def __init__(self, u, v):
        self.vertices = [u, v]


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo


class GrafoBipartido:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.X = []
        self.Y = []

    # Insere um vértice v em X
    def inserirX(self, v):
        self.X.append(v)

    # Insere um vértice v em Y
    def inserirY(self, v):
        self.Y.append(v)

    # Insere um vértice v já criado
    def inserirVertice(self, v):
        self.vertices.append(v)

    # Insere uma aresta entre os vértices u e v
    def inserirAresta(self, u, v):
        self.arestas.append(Aresta(u, v))

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

    # Carrega um grafo a partir de um arquivo
    def ler(self, arquivo):
        arq = open(arquivo, "r")

        qtVertices = int(arq.readline()[10:])
        for i in range(qtVertices):
            linha = arq.readline()
            linhaSplit = linha.split('"')
            indice = int(linha.split('"')[0])
            if len(linhaSplit) > 1:
                rotulo = linha.split('"')[1]
            else:
                rotulo = f"{indice}"
            v = Vertice(int(indice), rotulo)
            self.inserirVertice(v)

        arq.readline()

        for linha in arq:
            x, y = linha.split()
            xVertice = self.obterVertice(x)
            yVertice = self.obterVertice(y)
            self.inserirAresta(xVertice, yVertice)
            if (xVertice not in self.X) and (xVertice not in self.Y):
                self.inserirX(xVertice)
            if (yVertice not in self.X) and (yVertice not in self.Y):
                self.inserirY(yVertice)

        arq.close()
