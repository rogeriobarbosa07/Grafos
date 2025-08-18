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

    def bellmann_ford(self, inicial):
        matriz_copia = copy.deepcopy(self.matriz)
        atual = inicial

        valores_vertices = [float('inf')] * self.numero_vertices
        valores_vertices[inicial] = 0

        for i in range(self.numero_vertices - 1):
            # acumulador: se baseia no peso atual do vértice para setar o valor dos próximos
            peso_atual = valores_vertices[atual]

            for j in range(self.numero_vertices):
                if ((matriz_copia[atual][j] + peso_atual) < valores_vertices[j]) and matriz_copia[atual][j] != 0:
                    valores_vertices[j] = matriz_copia[atual][j] + peso_atual

            # escolhe quem tem o menor peso localmente para dar continuidade
            aux_valores = copy.deepcopy(valores_vertices)
            possiveis_posicoes = []
            for a in range(self.numero_vertices):
                if matriz_copia[atual][a] != 0:
                    possiveis_posicoes.append(a)
            menor_atual = min(aux_valores)
            for k in range(self.numero_vertices):
                if (aux_valores[k] == menor_atual) and (k in possiveis_posicoes):
                    atual = k
                else:
                    aux_valores[k] = float('inf')
                    menor_atual = min(aux_valores)

        print(valores_vertices)

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
grafo.bellmann_ford(0)