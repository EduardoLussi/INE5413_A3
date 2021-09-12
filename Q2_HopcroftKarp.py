from math import inf
from queue import Queue
from grafoBipartido import GrafoBipartido

def HopcroftKarp(G):
    tamanho = G.qtdVertices()

    D = [inf] * (tamanho + 1)  # Distâncias
    mate = [None] * tamanho  # Casamentos

    m = 0

    while BFS(G, mate, D):
        for x in G.X:
            if mate[x.indice - 1] is None:
                if DFS(G, mate, x, D):
                    m += 1

    return m, mate, D


def BFS(G, mate, D):
    Q = Queue()
    for x in G.X:
        if mate[x.indice - 1] is None:
            D[x.indice] = 0
            Q.put(x)
        else:
            D[x.indice] = inf

    D[0] = inf
    while not Q.empty():
        x = Q.get()
        if D[x.indice] < D[0]:
            for y in G.vizinhos(x):
                pos = mate[y.indice - 1]
                if pos is not None:
                    if D[pos.indice] == inf:
                        D[pos.indice] = D[x.indice] + 1
                        Q.put(mate[y.indice - 1])
                else:
                    D[0] = D[x.indice] + 1
    return not D[0] == inf


def DFS(G, mate, x, D):
    if x is not None:
        for y in G.vizinhos(x):
            pos = mate[y.indice - 1]
            if pos is not None:
                if D[pos.indice] == D[x.indice] + 1:
                    if DFS(G, mate, mate[y.indice - 1], D):
                        mate[y.indice - 1] = x
                        mate[x.indice - 1] = y
                        return True
            else:
                mate[y.indice - 1] = x
                mate[x.indice - 1] = y
                return True
        D[x.indice] = inf
        return False

    return True


grafo = GrafoBipartido()
grafo.ler("GrafosTeste/gr128_10.net")
retorno = HopcroftKarp(grafo)
print(retorno[0])
for a in retorno[1]:
    print(a.indice, end=" ")