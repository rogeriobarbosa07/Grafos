import copy

class GrafoEmMatriz:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.matriz = [[0] * numero_vertices for _ in range(numero_vertices)]

    def adiciona_aresta(self, vertice1, vertice2):
        self.matriz[vertice1][vertice2] = 1
        self.matriz[vertice2][vertice1] = 1

    def grau(self, vertice):
        return sum(self.matriz[vertice])

    def imprimir_matriz(self):
        print("Matriz de adjacência:")
        for linha in self.matriz:
            print(linha)

    def possui_ciclo_euleriano(self):
        for v in range(self.numero_vertices):
            if self.grau(v) % 2 != 0:
                return False
        return True

    def remove_aresta(self, matriz, vertice1, vertice2):
        matriz[vertice1][vertice2] = 0
        matriz[vertice2][vertice1] = 0

    def conta_componentes(self, matriz, visitado, vertice):
        visitado[vertice] = True
        for u in range(self.numero_vertices):
            if matriz[vertice][u] and not visitado[u]:
                self.conta_componentes(matriz, visitado, u)

    def eh_ponte(self, matriz, vertice1, vertice2):
        if matriz[vertice1][vertice2] == 0:
            return False

        visitado = [False] * self.numero_vertices
        self.conta_componentes(matriz, visitado, vertice1)
        antes = sum(visitado)

        self.remove_aresta(matriz, vertice1, vertice2)
        visitado = [False] * self.numero_vertices
        self.conta_componentes(matriz, visitado, vertice1)
        depois = sum(visitado)

        matriz[vertice1][vertice2] = 1
        matriz[vertice2][vertice1] = 1

        return depois < antes

    def matriz_zerada(self, matriz):
        for i in range(self.numero_vertices):
            for j in range(self.numero_vertices):
                if matriz[i][j] == 1:
                    return False
        return True

    def fleury(self, inicio):
        if not self.possui_ciclo_euleriano():
            print("O grafo não possui ciclo euleriano (há vértices de grau ímpar).")
            return

        matriz_copia = copy.deepcopy(self.matriz)
        atual = inicio
        caminho_de_vertices = [atual]
        caminho_de_arestas = []

        while not self.matriz_zerada(matriz_copia):
            for i in range(self.numero_vertices):
                if matriz_copia[atual][i]:
                    if not self.eh_ponte(matriz_copia, atual, i) or all(self.eh_ponte(matriz_copia, atual, j) == True for j in range(self.numero_vertices) if matriz_copia[atual][j]):
                        self.remove_aresta(matriz_copia, atual, i)
                        anterior = atual
                        atual = i
                        caminho_de_vertices.append(atual)
                        caminho_de_arestas.append((anterior, atual))
                        break

        print("Ciclo de Euler em Vértices:", caminho_de_vertices, "\nCiclo de Euler em Arestas:", caminho_de_arestas)


grafo = GrafoEmMatriz(7)
grafo.adiciona_aresta(0, 1)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(0, 3)
grafo.adiciona_aresta(0, 4)
grafo.adiciona_aresta(0, 5)
grafo.adiciona_aresta(0, 6)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(1, 4)
grafo.adiciona_aresta(1, 5)
grafo.adiciona_aresta(1, 6)
grafo.adiciona_aresta(2, 4)
grafo.adiciona_aresta(2, 5)
grafo.adiciona_aresta(2, 6)
grafo.adiciona_aresta(3, 2)
grafo.adiciona_aresta(3, 4)
grafo.adiciona_aresta(3, 5)
grafo.adiciona_aresta(3, 6)
grafo.adiciona_aresta(4, 5)
grafo.adiciona_aresta(4, 6)
grafo.adiciona_aresta(5, 6)
grafo.imprimir_matriz()
grafo.fleury(5)