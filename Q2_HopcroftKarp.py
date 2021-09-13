from math import inf
from queue import Queue

def HopcroftKarp(G):
    tamanho = G.qtdVertices()

    D = [inf] * (tamanho + 1)  # Distâncias
    mate = [None] * tamanho  # Casamentos (Parceiro de v)

    m = 0  # Quantidade de emparelhamento

    while BFS(G, mate, D):
        for x in G.X:
            if mate[x.indice - 1] is None:  # Se x não possui um parceiro
                if DFS(G, mate, x, D):
                    m += 1

    return m, mate, D


# Busca em largura com mais de um ponto de origem
def BFS(G, mate, D):
    Q = Queue()
    for x in G.X:
        if mate[x.indice - 1] is None:  # Se o vértice está livre (sem parceiro)
            D[x.indice] = 0
            Q.put(x)
        else:  # Se o vértice não está livre (possui parceiro)
            D[x.indice] = inf

    D[0] = inf  # Vértice artificial
    while not Q.empty():
        x = Q.get()
        if D[x.indice] < D[0]:
            for y in G.vizinhos(x):  # Para cada vizinho de x
                pos = mate[y.indice - 1]
                if pos is not None:  # Se y possui um parceiro não nulo
                    if D[pos.indice] == inf:
                        D[pos.indice] = D[x.indice] + 1
                        Q.put(mate[y.indice - 1])
                else:  # Se y possui um parceiro nulo
                    D[0] = D[x.indice] + 1
    # Se o vértice artificial permancer inalterado, não foi encontrado um caminho aumentante alternante
    return not D[0] == inf


def DFS(G, mate, x, D):
    if x is not None:  # Se x não for nulo
        for y in G.vizinhos(x):  # Para cada vizinho de x
            pos = mate[y.indice - 1]
            if pos is not None:  # Se y possui um parceiro não nulo
                if D[pos.indice] == D[x.indice] + 1:
                    if DFS(G, mate, mate[y.indice - 1], D):
                        # Faz o casamento x com y
                        mate[y.indice - 1] = x
                        mate[x.indice - 1] = y
                        return True
            else:  # Se y possui um parceiro nulo
                # Faz o casamento x com y
                mate[y.indice - 1] = x
                mate[x.indice - 1] = y
                return True
        D[x.indice] = inf
        return False

    return True
