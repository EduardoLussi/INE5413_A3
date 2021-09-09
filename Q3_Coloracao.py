from grafoNaoDirigido import GrafoNaoDirigido
from itertools import combinations
from math import inf

# Retorna todas as combinações possíveis de vértices de G
def obterCombinacoesVertices(G):
    S = [[si for si in s] for s in combinations(G.vertices, 0)] # Combinação de 0 elementos
    for i in range(1, G.qtdVertices() + 1): # Adiciona combinações de 1 até |V| elementos
        S.extend([[si for si in s] for s in combinations(G.vertices, i)])

    return S

# Retorna uma lista de subconjuntos de vértices independentes maximais
def obterIndependentesMax(G):
    # Obtém todos os subconjuntos possíveis de vértices
    S = obterCombinacoesVertices(G)[::-1]

    I = []  # Lista de conjuntos de vértices independentes

    for s in S: # Testa se cada subconjunto de S é independente
        # Se já foi encontrado um subconjunto independente de tamanho maior,
        # os subconjuntos maximais já foram encontrados
        if len(I) > 0:
            if len(s) < len(I[0]):
                break

        # Obtém cada par de vértice possível para o subconjunto s
        comb = [[ci for ci in c] for c in combinations(s, 2)]

        ind = True

        for c in comb:  # Verifica se existe aresta para cada par de vértice
            if G.haAresta(c[0], c[1]):
                ind = False  # Conjunto não é independente
                break
        
        if ind: # Se o subconjunto for independente, adiciona na lista
            I.append(s)

    return I


def Lawler(G):
    X = [0]
    C = [{}]
    S = obterCombinacoesVertices(G)
    
    for Si in S[1:]:  # Para cada combinação de vértices sem o vazio
        
        X.append(inf)
        C.append({})
        G1 = GrafoNaoDirigido()
        G1.vertices = Si

        # Obtém combinações de dois vértices candidados a uma aresta
        comb = [[ci for ci in c] for c in combinations(G1.vertices, 2)]
        for c in comb:  # Adiciona aresta em comum entre G1 com G
            if G.haAresta(c[0], c[1]):
                G1.inserirAresta(c[0], c[1], 1)

        IndMax = obterIndependentesMax(G1)  # Independentes Maximais
        for I in IndMax:
            SiSemI = [si for si in Si if si not in I]   # S\I
            i = S.index(SiSemI) # f(S\I)
            if X[i] + 1 < X[S.index(Si)]:
                X[S.index(Si)] = X[i] + 1
                C[S.index(Si)] = C[i].copy()    # Determina cores dos vértices
                for Ii in I:
                    C[S.index(Si)][Ii] = X[i] + 1

    print(f"São necessárias {X[-1]} cores para colorir o grafo:")

    # Imprime cores de cada vértice
    strCorVertices = "" 
    for v, i in C[-1].items():
        strCorVertices += f"{v.rotulo}: {i}, "
    print(strCorVertices[:-2])   

    return X[-1]
        

G = GrafoNaoDirigido()
G.ler("GrafosTeste/cor3.net")
Lawler(G)