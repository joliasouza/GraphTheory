class Grafo:
    # método construtor
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.matriz = [[0]*n_vertices for _ in range(n_vertices)]

    # lê a matriz de adjacência
    def adiciona_no(self, x, y):
        if 0 <= x < self.n_vertices and 0 <= y < self.n_vertices:
            self.matriz[x][y] = 1
            self.matriz[y][x] = 1 # grafo uni-direcional
        else:
            print("Vértice inválido.")

    def print_matriz(self):
        for row in self.matriz:
            print(" ".join(str(value) for value in row))

    # calcula o grau
    def grau(self, x):
        return sum(self.matriz[x])  # soma os valores da linha x
    
    # verifica se é ciclo
    def ciclo(self):
        # verifica se todos os vértices possuem grau 2
        for x in range(self.n_vertices):  
            if self.grau(x) != 2:
                return False
        return True
    
    def completo(self):
        n = self.n_vertices
        for i in range(n):
            for j in range(i + 1, n):
                if self.matriz[i][j] == 0:
                    return False
        return True
    
    def roda(self):
        n = self.n_vertices
        if n <= 3:
            return False

        # encontrar o nó central (degree n-1)
        no_central = -1
        for i in range(n):
            if self.grau(i) == n - 1:
                no_central = i
                break

        if no_central == -1:
            return False  # No hub vertex found

        # Check if the remaining vertices form a cycle
        cycle_vertices = [i for i in range(n) if i != no_central]
        for i in cycle_vertices:
            if self.degree(i) != 3:
                return False

        # Check if the cycle vertices are connected in a cycle
        for i in range(len(cycle_vertices)):
            v1 = cycle_vertices[i]
            v2 = cycle_vertices[(i + 1) % len(cycle_vertices)],
            if self.matrix[v1][v2] == 0:
                return False

        return True

    def is_eulerian(self):
        # check if all vertices have an even degree
        for v in range(self.n_vertices):
            if self.degree(v) % 2 != 0:
                return False
        return True
    
    def is_isomorphic(self, other):
        if self.n_vertices != other.n_vertices:
            return False

        # Check if the degrees of the vertices match
    
    
    """
    Exercicios:
        Classificar:
            Cn - ciclo
                todo vertice deve possuir grau par
            Kn - grafo completo
                um grafo onde todos os seus vértices tem o grau máximo.
                Ou seja, existe aresta presente entre todos os pares de vértices.
            Wn - grafo roda
                um grafo que é um ciclo onde um vértice é conectado a todos os outros vértices.
            Grafo Euleriano
                um grafo onde todos os vértices possuem grau par.
            Isomorfo
    """
