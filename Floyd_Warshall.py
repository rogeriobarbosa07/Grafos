import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[float('inf')] * numero_vertices for _ in range(numero_vertices)]
        self.arestas = []

    def adiciona_aresta_peso(self, vertice1, vertice2, peso):
        self.arestas.append((vertice1, vertice2, peso))

    def imprime_matriz(self):
        for linha in self.matriz:
            print(linha)

    def peso_aresta(self, v, w):
        for i in self.arestas:
            if i[0] == v and i[1] == w:
                return i[2]
        return float('inf')

    def floyd_warshall(self):
        pi = [None] * self.numero_vertices

        for v in range(self.numero_vertices):
            for w in range(self.numero_vertices):
                if v == w:
                    self.matriz[v][w] = 0
                else:
                    self.matriz[v][w] = self.peso_aresta(v, w)

        print("Matriz antes:")
        self.imprime_matriz()

        for k in range(self.numero_vertices):
            for v in range(self.numero_vertices):
                for w in range(self.numero_vertices):
                    if self.matriz[v][w] > self.matriz[v][k] + self.matriz[k][w]:
                        self.matriz[v][w] = self.matriz[v][k] + self.matriz[k][w]
                        pi[w] = k

        print('\nMatriz depois:')
        self.imprime_matriz()        
    
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