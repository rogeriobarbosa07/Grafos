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
            if self.matriz[vertice][i] == 1 and i != vertice:
                grau += 1
        print(f"Grau do vértice {vertice}: {grau}")
    
grafo = GrafoEmMatriz(4)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(2, 2)
grafo.adiciona_aresta(2, 3)
grafo.adiciona_aresta(3, 1)
grafo.imprime_matriz()
grafo.imprime_arestas()
grafo.imprime_grau(2)