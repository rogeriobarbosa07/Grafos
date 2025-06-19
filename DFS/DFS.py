import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[0] * numero_vertices for _ in range(numero_vertices)]
        self.arestas = []

    def adiciona_aresta(self, vertice1, vertice2):
        self.matriz[vertice1][vertice2] = 1
        self.matriz[vertice2][vertice1] = 1
        self.arestas.append((vertice1, vertice2))
        self.arestas.append((vertice2, vertice1))

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

    def remove_vertice(self, matriz, vertice):
        for i in range(self.numero_vertices):
            matriz[vertice][i] = 0
            matriz[i][vertice] = 0

    def inicia_DFS(self, vertice):
        self.matriz_copia = copy.deepcopy(self.matriz)

        self.cor = ['b'] * self.numero_vertices
        self.pi = [None] * self.numero_vertices
        self.d = [0] * self.numero_vertices
        self.f = [0] * self.numero_vertices

        self.cor[vertice] = 'c'
        self.d[vertice] = 1

        for i in range(self.numero_vertices):
            if i != 0:
                self.DFS(vertice, i)
                break

    def DFS(self, v_anterior, v_atual):
        self.pi[v_atual] = 'c'
        self.pi[v_atual] = v_anterior
        self.d[v_atual] = max(self.d, self.f)

        if max(self.matriz_copia[v_atual]) == 0:
            self.f[v_atual] = max(self.d, self.f) + 1
            self.cor[v_atual] = 'p'
        else:
            for i in range(self.numero_vertices):
                if i == 1:
                    self.DFS(v_atual, i)
                    self.f[v_atual] = max(self.d, self.f) + 1
                    self.cor[v_atual] = 'p'

grafo = GrafoEmMatriz(5)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(2, 2)
grafo.adiciona_aresta(2, 3)
grafo.adiciona_aresta(3, 1)
grafo.adiciona_aresta(4, 0)
grafo.adiciona_aresta(4, 1)
grafo.adiciona_aresta(4, 2)
grafo.adiciona_aresta(4, 4)
grafo.imprime_matriz()
grafo.imprime_arestas()