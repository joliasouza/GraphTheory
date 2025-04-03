"""
Reconhecendo Grafos I
    Dado um Grafo Conexo representado por uma quantidade de vértices N , uma quantidade de arestas
    M e uma lista de arestas, imprima 1 caso este grafo seja um ciclo, 2 caso este grafo seja uma roda, 3
    caso este grafo seja um grafo completo e -1 caso não seja nenhum dos 3. Cada vértice será representado
    por um índice e cada aresta será representada por um par de índices.
Entrada
    A entrada conterá M + 1 linhas. A primeira linha conterá dois valores N e M representando
    respectivamente a quantidade de vértices e a quantidade de arestas.
    As próximas M linhas conterão dois inteiros u e v com valores entre 1 e N representando as arestas
    do grafo.
    É garantido que o numero de vertices N na entrada é maior que 3.
Saída
    A saída deverá conter um inteiro seguindo as definições especificadas no problema.
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
    
    # calcula o grau
    def grau(self, x):
        return sum(self.matriz[x])  # soma os valores da linha x

    def print_matriz(self):
        for row in self.matriz:
            print(" ".join(str(value) for value in row))
    
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


    
def main():
    # n = vértices
    # m = arestas
    n, m = map(int, input().split())

    if n > 3:
        g = Grafo(n)
        for i in range(m):
            x, y = map(int, input().split())
            g.adiciona_no(x-1, y-1)

        #g.print_matriz()
        
        if g.ciclo():
            print(1)

        elif g.roda():
            print(2)

        elif g.completo():
            print(3)

        else:
            print(-1)

    else:
        print("Número de vértices inválido.")
            
"""
1 - Ciclo
2 - Roda
3 - Completo
"""

if __name__ == "__main__":
    main()
