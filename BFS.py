import copy, queue

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

    def remove_aresta(self, vertice1, vertice2):
        self.matriz_copia[vertice1][vertice2] = 0
        self.matriz_copia[vertice2][vertice1] = 0

    def fila_para_lista(self):
        lista = []
        temporario = queue.Queue()

        while not self.fila.empty():
            item = self.fila.get()
            lista.append(item)
            temporario.put(item)

        while not temporario.empty():
            self.fila.put(temporario.get())

        return lista

    def imprime_visitado(self, vertice):
        print(f"\nBFS({vertice}):\ncor[{vertice}] = {self.cor[vertice]}\npi[{vertice}] = {self.pi[vertice]}\nd[{vertice}] = {self.d[vertice]}")

    def BFS(self, vertice):
        self.matriz_copia = copy.deepcopy(self.matriz)

        self.cor = ['b'] * self.numero_vertices
        self.pi = [None] * self.numero_vertices
        self.d = [0] * self.numero_vertices
        self.fila = queue.Queue()

        self.cor[vertice] = 'c'
        self.fila.put(vertice)
        
        print(f"\nfila = {self.fila_para_lista()}")

        while not self.fila.empty():
            for i in range(self.numero_vertices):
                if self.matriz_copia[vertice][i] == 1 and self.cor[i] == 'b':
                    self.cor[i] = 'c'
                    self.pi[i] = vertice
                    self.d[i] = self.d[vertice] + 1
                    self.fila.put(i)
                    self.remove_aresta(vertice, i)

            vertice = self.fila.get()
            self.imprime_visitado(vertice)

            print(f"fila = {self.fila_para_lista()}")
    
grafo = GrafoEmMatriz(4)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(2, 2)
grafo.adiciona_aresta(2, 3)
grafo.adiciona_aresta(3, 0)
grafo.adiciona_aresta(3, 1)
grafo.imprime_matriz()
grafo.BFS(1)
