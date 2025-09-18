# A program to implement Depth-First Search (DFS) for graph traversal.

def dfs(graph, start_node, visited=None):
    """
    Performs a Depth-First Search traversal on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node: The starting node for the traversal.
        visited (set): A set to keep track of visited nodes to avoid cycles.
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node, end=' ')

    # Recursively visit all unvisited neighbors
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == "__main__":
    # Define a sample graph using an adjacency list
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DFS traversal starting from node 'A':")
    dfs(sample_graph, 'A')
    print("\n")
