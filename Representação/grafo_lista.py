class GrafoEmLista:
    def __init__(self, numero_vertices):
        self.numero_vertices = numero_vertices
        self.lista = [[] for _ in range(numero_vertices)]
        self.arestas = []

    def adiciona_aresta(self, vertice1, vertice2):
        if vertice2 not in self.lista[vertice1]:
            self.lista[vertice1].append(vertice2)
            self.arestas.append((vertice1, vertice2))
        if vertice1 not in self.lista[vertice2]:
            self.lista[vertice2].append(vertice1)
            self.arestas.append((vertice2, vertice1))

    def imprime_lista(self):
        print("Lista de Adjacência:")
        i = 0
        for l in self.lista:
            print(f"{i}: {l}")
            i += 1

    def imprime_arestas(self):
        print("Conjunto de arestas do grafo:", self.arestas)

    def imprime_grau(self, vertice):
        print(f"Grau do vértice {vertice}: {len(self.lista[vertice])}")


grafo = GrafoEmLista(4)
grafo.adiciona_aresta(2, 3)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(0, 2)
grafo.imprime_lista()
grafo.imprime_arestas()
grafo.imprime_grau(2)