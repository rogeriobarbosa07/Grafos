import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[0] * numero_vertices for _ in range(numero_vertices)]
    
    def adiciona_aresta_peso(self, vertice1, vertice2, peso):
        self.matriz[vertice1][vertice2] = peso
        self.matriz[vertice2][vertice1] = peso

    def imprimir_matriz(self):
        print("Matriz de adjacência:")
        for linha in self.matriz:
            print(linha)

    def grau(self, vertice):
        return sum(self.matriz[vertice])

    def remove_vertice(self, matriz, vertice):
        for i in range(self.numero_vertices):
            matriz[vertice][i] = 0
            matriz[i][vertice] = 0

    def bellmore_neuhauser(self, inicial):
        matriz_copia = copy.deepcopy(self.matriz)
        H = [inicial]
        atual = inicial

        while len(H) < self.numero_vertices:
            vizinhos = []
            for i, peso in enumerate(matriz_copia[atual]):
                if peso != 0 and i not in H:
                    vizinhos.append((i, peso))

            if not vizinhos:
                break  

            proximo = min(vizinhos, key=lambda x: x[1])[0]
            H.append(proximo)
            self.remove_vertice(matriz_copia, atual)
            atual = proximo

        if len(H) < self.numero_vertices or self.matriz[H[self.numero_vertices - 1]][inicial] == 0:
            H.append("X")
            print("Não foi possível encontrar o caminho:", H)
        else:
            H.append(inicial)
            print("Caminho aproximado (Bellmore-Neuhauser):", H)
            
grafo = GrafoEmMatriz(7)
grafo.adiciona_aresta_peso(0, 1, 3)
grafo.adiciona_aresta_peso(0, 3, 5)
grafo.adiciona_aresta_peso(0, 5, 8)
grafo.adiciona_aresta_peso(1, 2, 9)
grafo.adiciona_aresta_peso(1, 4, 5)
grafo.adiciona_aresta_peso(1, 6, 8)
grafo.adiciona_aresta_peso(2, 4, 9)
grafo.adiciona_aresta_peso(2, 6, 11)
grafo.adiciona_aresta_peso(3, 5, 9)
grafo.adiciona_aresta_peso(4, 5, 3)
grafo.adiciona_aresta_peso(5, 6, 9)
grafo.imprimir_matriz()
grafo.bellmore_neuhauser(5)