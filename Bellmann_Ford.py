import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[0] * numero_vertices for _ in range(numero_vertices)]
        self.arestas = []

    def adiciona_aresta_peso(self, vertice1, vertice2, peso):
        self.matriz[vertice1][vertice2] = peso
        self.arestas.append((vertice1, vertice2, peso))

    def imprime_matriz(self):
        print("Matriz de adjacência:")
        for linha in self.matriz:
            print(linha)

    def imprime_arestas(self):
        print("Conjunto de arestas do grafo (com pesos):", self.arestas)

    def imprime_grau(self, vertice):
        grau = 0
        for i in range(self.numero_vertices):
            if self.matriz[vertice][i] == 1:
                if i == vertice:
                    grau += 1
                grau += 1
        print(f"Grau do vértice {vertice}: {grau}")

    def bellman_ford(self, inicial):
        dist = [float("inf")] * self.numero_vertices
        dist[inicial] = 0

        for _ in range(self.numero_vertices - 1):
            for u, v, peso in self.arestas:
                if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso

        for u, v, peso in self.arestas:
            if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                print("Grafo contém ciclo de peso negativo!")
                return None

        return dist

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

grafo.imprime_matriz()
grafo.bellman_ford(0)
