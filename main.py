from graph_algorithms import read_adjacency_matrix, is_directed, dijkstra

def main():
    file_path = 'adjacency_matrix.csv' 
    adjacency_matrix = read_adjacency_matrix(file_path)
    
    # Determina se il grafo è orientato
    directed = is_directed(adjacency_matrix)
    print(f"Il grafo è {'orientato' if directed else 'non orientato'}.")

    # Applicazione l'algoritmo di Dijkstra
    start_node = 0 
    distances = dijkstra(adjacency_matrix, start_node)
    print(f"Distanze dal nodo {start_node}: {distances}")

if __name__ == "__main__":
    main()