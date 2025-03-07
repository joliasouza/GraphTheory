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

def main():
    # n = vértices
    # m = arestas
    n, m = input()
    g = Grafo(n)
    for i in range(m):
        x, y = input()
        g.adiciona_no(x, y)


if __name__ == "__main__":
    main()