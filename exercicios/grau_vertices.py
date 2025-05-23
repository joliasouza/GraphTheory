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

    def print_matriz(self):
        for row in self.matriz:
            print(" ".join(str(value) for value in row))

def main():
    # n = vértices
    # m = arestas
    n, m = map(int, input().split())
    g = Grafo(n)

    for i in range(m):
        x, y = map(int, input().split())
        g.adiciona_no(x-1, y-1)

    for i in range(n):
        if i < n-1:
            print(g.grau(x-1), end=" ")
        else:
            print(g.grau(x-1))


if __name__ == "__main__":
    main()
