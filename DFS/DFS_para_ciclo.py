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

    def remove_aresta(self, vertice1, vertice2):
        self.matriz_copia[vertice1][vertice2] = 0
        self.matriz_copia[vertice2][vertice1] = 0

    def imprime_visitado(self, vertice):
        print(f"\nDFS({vertice}):\ncor[{vertice}] = {self.cor[vertice]}\npi[{vertice}] = {self.pi[vertice]}\nd[{vertice}] = {self.d[vertice]}\nf[{vertice}] = {self.f[vertice]}")

    def DFS(self, vertice):
        self.matriz_copia = copy.deepcopy(self.matriz)

        self.cor = ['b'] * self.numero_vertices
        self.pi = [None] * self.numero_vertices
        self.d = [0] * self.numero_vertices
        self.f = [0] * self.numero_vertices

        self.cor[vertice] = 'c'
        self.d[vertice] = 1
        
        # Trecho mais importante: loop de execução do DFS
        for i in range(self.numero_vertices):
            if self.matriz_copia[vertice][i] != 0 and self.cor[i] == 'b':
                self.imprime_visitado(vertice)
                self.DFS_visita(vertice, i)

        self.cor[vertice] = 'c'
        self.f[vertice] = max(max(self.d), max(self.f)) + 1

        self.imprime_visitado(vertice)

    def DFS_visita(self, v_anterior, v_atual):
        self.remove_aresta(v_anterior, v_atual)

        self.cor[v_atual] = 'c'
        self.pi[v_atual] = v_anterior
        self.d[v_atual] = max(max(self.d), max(self.f)) + 1

        self.imprime_visitado(v_atual)

        for i in range(self.numero_vertices):
            if self.matriz_copia[v_atual][i] != 0 and self.cor[i] in ('c', 'p'):
                    print("Ciclo encontrado!")
                    break
            elif self.matriz_copia[v_atual][i] != 0 and self.cor[i] == 'b':
                self.DFS_visita(v_atual, i)

        self.cor[v_atual] = 'p'
        self.f[v_atual] = max(max(self.d), max(self.f)) + 1

        self.imprime_visitado(v_atual)

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
grafo.DFS(3)