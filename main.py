from grafoDirigido import GrafoDirigido
from grafoNaoDirigido import GrafoNaoDirigido
from grafoBipartido import GrafoBipartido

from Q1_EdmondsKarp import FordFulkerson
from Q2_HopcroftKarp import HopcroftKarp
from Q3_Coloracao import Lawler

op = 1
while op in range(1, 4):
    print(f"\n{'-'*50}")
    print("1- Edmonds-Karp")
    print("2- Hopcroft-Karp")
    print("3- Coloração de Vértices")
    print("4- Sair")
    print(f"{'-' * 50}\n")

    op = int(input("Digite o número da questão: "))

    if op not in range(1, 4):
        break

    name = input("Digite o nome do arquivo: ")   # Inserir arquivo de teste na pasta GrafosTeste

    print()

    if op == 1:
        grafo = GrafoDirigido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
            # Recebe grafo e vértice de origem e destino
            FordFulkerson(grafo, grafo.obterVertice(2), grafo.obterVertice(5))
        except:
            print("Nome de arquivo inválido")
        
    elif op == 2:
        grafo = GrafoBipartido()

        try: 
            grafo.ler(f"GrafosTeste/{name}")
            retorno = HopcroftKarp(grafo)
            print(retorno[0])
            for a in retorno[1]:
                print(a.indice, end=" ")
            print()
        except:
            print("Nome de arquivo inválido")

    elif op == 3:
        grafo = GrafoNaoDirigido()
        
        try: 
            grafo.ler(f"GrafosTeste/{name}")
            Lawler(grafo)
        except:
            print("Nome de arquivo inválido")
    else:
        break
