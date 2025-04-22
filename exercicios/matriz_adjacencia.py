""""
Matriz de Adjacencia
    Dado um Grafo representado por uma quantidade de vértices N , uma quantidade de arestas M e
    uma lista de arestas, imprima a sua matriz de adjacência. Cada vértice será representado por um índice
    e cada aresta será representada por um par de índices.
Entrada
    A entrada conterá M + 1 linhas. A primeira linha conterá dois valores N e M representando
    respectivamente a quantidade de vértices e a quantidade de arestas.
    As próximas M + 1 linhas conterão dois inteiros u e v com valores entre 1 e N representando as
    arestas do grafo.
Saída
    A saída deverá conter N linhas cada uma com N colunas representado a matriz de adjacência do
    grafo.
"""
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
    n, m = map(int, input().split())
    g = Grafo(n)

    for i in range(m):
        x, y = map(int, input().split())
        g.adiciona_no(x-1, y-1)

    g.print_matriz()


if __name__ == "__main__":
    main()
