import itertools

def solve_tsp_brute_force(graph):

    nodes = list(graph.keys())
    start_node = nodes[0]
    other_nodes = nodes[1:]
    
    shortest_path = None
    min_distance = float('inf')
    
    # Generate all possible permutations of the other nodes
    for perm in itertools.permutations(other_nodes):
        current_path = [start_node] + list(perm) + [start_node]
        current_distance = 0
        
        # Calculate the distance for the current path
        for i in range(len(current_path) - 1):
            from_node = current_path[i]
            to_node = current_path[i+1]
            current_distance += graph[from_node][to_node]
        
        # Update if a shorter path is found
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = current_path
            
    return shortest_path, min_distance

# Example Usage
if __name__ == "__main__":
    # Define a sample graph with distances between cities
    # Distances are assumed to be symmetric (e.g., A-B is same as B-A)
    # The example graph is represented as an adjacency matrix
    city_graph = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }

    path, distance = solve_tsp_brute_force(city_graph)
    print("Shortest path found:", " -> ".join(path))
    print("Minimum distance:", distance)