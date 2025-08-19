import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[0] * numero_vertices for _ in range(numero_vertices)]
        self.arestas = []

    def adiciona_aresta_peso(self, vertice1, vertice2, peso):
        self.matriz[vertice1][vertice2] = 1
        self.arestas.append((vertice1, vertice2, peso))

    def imprime_matriz(self):
        print("Matriz de adjacência:")
        for linha in self.matriz:
            print(linha)

    def imprime_arestas(self):
        print("Conjunto de arestas do grafo:", self.arestas)

    def imprime_grau(self, vertice):
        grau = 0
        for i in range(self.numero_vertices):
            if self.matriz[vertice][i] == 1:
                if i == vertice:
                    grau += 1
                grau += 1
        print(f"Grau do vértice {vertice}: {grau}")

    def peso_aresta(self, v, w):
        for i in self.arestas:
            if i[0] == v and i[1] == w:
                return i[2]
        return float('inf')

    def floyd_warshall(self):
        matriz_pesos = [[float('inf')] * self.numero_vertices for _ in range (self.numero_vertices)]
        pi = [None] * self.numero_vertices

        for v in range(self.numero_vertices):
            for w in range(self.numero_vertices):
                if v == w:
                    matriz_pesos[v][w] = 0
                else:
                    matriz_pesos[v][w] = self.peso_aresta(v, w)

        print("Matriz antes:\n", matriz_pesos)

        for k in range(self.numero_vertices):
            for v in range(self.numero_vertices):
                for w in range(self.numero_vertices):
                    if matriz_pesos[v][w] > matriz_pesos[v][k] + matriz_pesos[k, w]:
                        matriz_pesos[v][w] = matriz_pesos[v][k] + matriz_pesos[k][w]
                        pi[w] = k

        print('\nMatriz depois:\n', matriz_pesos)
    
grafo = GrafoEmMatriz(5)
grafo.adiciona_aresta_peso(0, 1, 7)
grafo.adiciona_aresta_peso(0, 2, 6)
grafo.adiciona_aresta_peso(1, 2, 8)
grafo.adiciona_aresta_peso(1, 3, 5)
grafo.adiciona_aresta_peso(1, 4, -4)
grafo.adiciona_aresta_peso(2, 3, -3)
grafo.adiciona_aresta_peso(2, 4, 9)
grafo.adiciona_aresta_peso(3, 1, -2)
grafo.adiciona_aresta_peso(4, 0, 2)
grafo.adiciona_aresta_peso(4, 3, 7)
grafo.floyd_warshall()