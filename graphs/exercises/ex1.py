from classes.graphClass import Graph

def exercicio1():
    n_vertices = int(input("Digite o número de matrizes: "))
    graph = Graph(n_vertices)

    while True:
        print("\n1. Adiciona vértice")
        print("2. Print matriz")
        print("3. Sair")
        option = int(input("Escolha uma opção: "))
        
        if option == 1:
            source = int(input("Digite o vértice de origem: "))
            destination = int(input("Digite o vértice de destino: "))
            graph.add_edge(source, destination)
        elif option == 2:
            graph.print_matrix()
        elif option == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")