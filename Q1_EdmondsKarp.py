from grafoDirigido import GrafoDirigido
from math import inf

def EdmondsKarp(G, s, t, Gf):
    C = [s] # Vértices visitados
    A = [None] * G.qtdVertices()  # Ancestrais
    
    Q = [s]  # Fila: iniciando busca pela fonte

    while len(Q) > 0:
        u = Q.pop(0)
        for v in G.vizinhos(u):
            if (not (v in C)) and Gf.peso(u, v) > 0:    # Ainda tem espaço?
                C.append(v) # v marcado como visitado
                A[G.vertices.index(v)] = u  # u é ancestral de v
                if v == t:  # Sorvedouro encontrado, Criar caminho aumentante
                    p = [t]
                    w = t
                    while w != s:
                        w = A[G.vertices.index(w)]
                        p.insert(0, w)
                    return p
                Q.append(v)
    
    return None

def getGrafoResidual(G):    # Copia G para o grafo residual Gf
    Gf = GrafoDirigido()

    Gf.vertices = G.vertices    # Vértices são os mesmos
    
    for arco in G.arcos:    # Copia arcos de G
        Gf.inserirArco(arco.origem, arco.destino, arco.peso)
    
    return Gf

def FordFulkerson(G, s, t):
    Gf = getGrafoResidual(G)

    fluxoMaximo = 0

    p = EdmondsKarp(G, s, t, Gf)
    while p:    # Enquanto existir um caminho aumentante p na rede residual de s a t
        menorPeso = inf
        for i in range(len(p)-1):   # Encontra menor peso do caminho p para Gf
            pesoAtual = Gf.peso(p[i], p[i+1])
            if pesoAtual < menorPeso:
                menorPeso = pesoAtual
        
        for i in range(len(p)-1):   # Atualiza grafo residual
            if G.haArco(p[i], p[i+1]):
                Gf.obterArco(p[i], p[i+1]).peso -= menorPeso
        
        fluxoMaximo += menorPeso
        p = EdmondsKarp(G, s, t, Gf)    # Encontra próximo caminho aumentante p
    
    print(f"Fluxo máximo: {fluxoMaximo}")
    return fluxoMaximo


grafo = GrafoDirigido()
grafo.ler("GrafosTeste/teste_de_mesa_FluxoMaximo.net")
# Recebe grafo e vértice de origem e destino
FordFulkerson(grafo, grafo.obterVertice(2), grafo.obterVertice(5))