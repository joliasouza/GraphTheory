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
    
    # calcula o grau
    def grau(self, x):
        return sum(self.matriz[x])  # soma os valores da linha x
    
    # verifica se é ciclo
    def ciclo(self):
        # verifica se todos os vértices possuem grau 2
        for x in range(self.n_vertices - 1):  
            if self.grau(x) != 2:
                return False
        return True
    
    def completo(self):
        n = self.n_vertices
        for i in range(n):
            for j in range(i, n - 1):
                if self.matriz[i][j] == 0 and i != j:
                    return False
        return True
    
    def roda(self):
        n = self.n_vertices

        # Se o grafo for completo, ele não pode ser considerado uma roda.
        if self.completo():
            return False

        # Procura o nó central, que deve ter grau n - 1.
        no_central = None
        for i in range(n):
            if self.grau(i) == n - 1:
                no_central = i
                break

        if no_central is None:
            return False

        # Verifica se todos os outros nós possuem grau exatamente 3.
        for i in range(n):
            if i != no_central and self.grau(i) != 3:
                return False

        return True
    
    def completo(self):
        n = self.n_vertices
        for i in range(n):
            for j in range(i, n - 1):
                if self.matriz[i][j] == 0 and i != j:
                    return False
        return True
    
    def complemento(self):
        n = self.n_vertices
        for i in range(n):
            if self.grau(i) < n-1:
                for j in range(n):
                    if i != j and self.matriz[i][j] == 0:
                        self.matriz[i][j] = 1
                        self.matriz[j][i] = 1
                        print(i+1, j+1)
    
    def ciclo_euleriano(self):
        for i in range(self.n_vertices):
            if self.grau(i) % 2 != 0:
                return False
        return True
    
    def caminho_euleriano(self):
        vertice_impar = 0
        for i in range(self.n_vertices):
            if self.grau(i) % 2 != 0:
                vertice_impar = vertice_impar + 1
        if vertice_impar == 0 or vertice_impar == 2:
            return True
        return False

    def print_matriz(self):
        for row in self.matriz:
            print(" ".join(str(value) for value in row))
