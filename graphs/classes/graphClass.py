class Graph:
    # constructor method
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.matrix = [[0]*n_vertices for _ in range(n_vertices)]

    # read the matrix
    def add_edge(self, x, y):
        if 0 <= x < self.n_vertices and 0 <= y < self.n_vertices:
            self.matrix[x][y] = 1
            self.matrix[y][x] = 1 # For an undirected graph
        else:
            print("Vértice inválido.")

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(str(value) for value in row))

    # calculate degree
    def degree(self, x):
        return sum(self.matrix[x])  # sum the values of row x
    
    # verify if is a cycle
    def is_cycle(self):
        # Checks if all vertices have a degree of 2
        for x in range(self.n_vertices):  
            if self.degree(x) != 2:
                return False
        return True  # If all vertices have a degree of 2, it is a cycle
    
    def is_complete(self):
        n = self.n_vertices
        for i in range(n):
            for j in range(i + 1, n):
                if self.matrix[i][j] == 0:
                    return False
        return True
    
    def is_wheel(self):
        n = self.n_vertices
        if n <= 3:
            return False

        # Find the hub vertex (degree n-1)
        hub = -1
        for i in range(n):
            if self.degree(i) == n - 1:
                hub = i
                break

        if hub == -1:
            return False  # No hub vertex found

        # Check if the remaining vertices form a cycle
        cycle_vertices = [i for i in range(n) if i != hub]
        for i in cycle_vertices:
            if self.degree(i) != 3:
                return False

        # Check if the cycle vertices are connected in a cycle
        for i in range(len(cycle_vertices)):
            v1 = cycle_vertices[i]
            v2 = cycle_vertices[(i + 1) % len(cycle_vertices)]
            if self.matrix[v1][v2] == 0:
                return False

        return True

    def is_eulerian(self):
        # check if all vertices have an even degree
        for v in range(self.n_vertices):
            if self.degree(v) % 2 != 0:
                return False
        return True
    
    
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
    """
