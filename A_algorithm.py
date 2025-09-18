import heapq

def a_star(graph, start, goal, heuristic):
    """
    Finds the shortest path from start to goal using the A* algorithm.

    Args:
        graph (dict): A dictionary representing the graph, where keys are nodes
                      and values are dictionaries of neighboring nodes and edge costs.
        start: The starting node.
        goal: The goal node.
        heuristic (func): A function that estimates the cost from a node to the goal.

    Returns:
        list: The path from start to goal, or None if no path exists.
    """
    
    open_set = [(0, start)]  # Priority queue: (f_score, node)
    came_from = {}
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current_node = heapq.heappop(open_set)
        
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1] # Return reversed path

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def heuristic_func(node, goal):
    """
    Simple heuristic function (Manhattan distance for a 2D grid).
    Assumes nodes are tuples of (x, y) coordinates.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Example Usage
if __name__ == "__main__":
    # Define a simple grid graph where nodes are (row, col) tuples
    example_graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (0, 2): 1, (1, 1): 1},
        (0, 2): {(0, 1): 1, (1, 2): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1},
        (1, 2): {(0, 2): 1, (1, 1): 1, (2, 2): 1},
        (2, 0): {(1, 0): 1, (2, 1): 1},
        (2, 1): {(1, 1): 1, (2, 0): 1, (2, 2): 1},
        (2, 2): {(1, 2): 1, (2, 1): 1}
    }
    
    start_node = (0, 0)
    goal_node = (2, 2)
    
    path = a_star(example_graph, start_node, goal_node, heuristic_func)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
