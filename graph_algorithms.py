import csv
import numpy as np
import heapq

def read_adjacency_matrix(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        matrix = [list(map(int, row)) for row in reader]
    return np.array(matrix)

def is_directed(adjacency_matrix):
    return not np.array_equal(adjacency_matrix, adjacency_matrix.T)

def dijkstra(adjacency_matrix, start_node):
    n = len(adjacency_matrix)
    distances = [float('inf')] * n
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in enumerate(adjacency_matrix[current_node]):
            if weight > 0: 
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances