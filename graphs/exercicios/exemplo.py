from graphs.classes.classeGrafo import Graph

def exemplo():
    # Teste
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)  # Forma um ciclo
    g.print_matrix()

    print("O grafo é um ciclo?", g.is_cycle())  # Deve imprimir True
    print("O grafo é completo?", g.is_complete())  # Deve imprimir False
    g.add_edge(0, 2)  # Agora não é um ciclo
    print("O grafo é um ciclo?", g.is_cycle())  # Deve imprimir False

    
    g.print_matrix()