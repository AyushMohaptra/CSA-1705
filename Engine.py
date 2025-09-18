# Engine.py
import heapq

def is_solvable(state):
    """
    Checks if a given 8-puzzle state is solvable.

    For a 3x3 grid, a state is solvable if the number of inversions is even.
    An inversion is any pair of tiles that are in the wrong order.
    """
    inversions = 0
    # Flatten the state, ignoring the empty space (0)
    flat_state = [tile for tile in state if tile != 0]
    
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
                
    return inversions % 2 == 0

def format_path_to_steps(path):
    """
    Converts a path of board states into a list of human-readable instructions.
    """
    steps = []
    for i in range(len(path) - 1):
        current_state = path[i]
        next_state = path[i+1]
        
        # Find the position of the empty tile (0) in both states
        zero_index_current = current_state.index(0)
        zero_index_next = next_state.index(0)
        
        # The tile that moved is the one at the empty spot's *next* position
        moved_tile = next_state[zero_index_current]
        
        # Determine the direction of the move
        row_diff = (zero_index_next // 3) - (zero_index_current // 3)
        col_diff = (zero_index_next % 3) - (zero_index_current % 3)
        
        direction = ""
        if row_diff == 1: direction = "UP"
        elif row_diff == -1: direction = "DOWN"
        elif col_diff == 1: direction = "LEFT"
        elif col_diff == -1: direction = "RIGHT"

        steps.append(f"Move {moved_tile} {direction}")
        
    return steps

class PuzzleSolver:
    """
    Encapsulates the logic for solving an 8-puzzle using the A* search algorithm.
    """
    def __init__(self, initial_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.goal_positions = {tile: (i // 3, i % 3) for i, tile in enumerate(self.goal_state)}

    def _calculate_manhattan_distance(self, state):
        distance = 0
        for i, tile in enumerate(state):
            if tile != 0:
                current_pos = (i // 3, i % 3)
                goal_pos = self.goal_positions[tile]
                distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        return distance

    def _get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        x, y = zero_index // 3, zero_index % 3
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = list(state)
                neighbor_index = nx * 3 + ny
                new_state[zero_index], new_state[neighbor_index] = new_state[neighbor_index], new_state[zero_index]
                neighbors.append(tuple(new_state))
        return neighbors

    def solve(self):
        """Finds the shortest solution path using the A* algorithm."""
        open_set = [(self._calculate_manhattan_distance(self.initial_state), self.initial_state)]
        came_from = {}
        g_score = {self.initial_state: 0}
        
        while open_set:
            _, current_state = heapq.heappop(open_set)
            if current_state == self.goal_state:
                path = []
                while current_state in came_from:
                    path.append(current_state)
                    current_state = came_from[current_state]
                path.append(self.initial_state)
                return path[::-1]

            for neighbor in self._get_neighbors(current_state):
                tentative_g_score = g_score[current_state] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current_state
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self._calculate_manhattan_distance(neighbor)
                    heapq.heappush(open_set, (f_score, neighbor))
        return None

def solve_puzzle(grid):
    """
    The main function that UI.py will call.

    Args:
        grid (numpy.ndarray): The 3x3 puzzle grid from the OCR module.

    Returns:
        list: A list of human-readable steps, or None if unsolvable.
    """
    # Convert the 2D NumPy array to a 1D tuple for the solver
    initial_state = tuple(grid.flatten())
    
    # First, check if the puzzle is solvable
    if not is_solvable(initial_state):
        print("Engine: This puzzle is not solvable.")
        return None

    # Create a solver instance and find the path
    solver = PuzzleSolver(initial_state)
    path = solver.solve()
    
    if path:
        # Convert the path of states into a list of instructions
        steps = format_path_to_steps(path)
        return steps
    
    return None

# You can add a test block here to run this file directly
if __name__ == '__main__':
    # This part will only run if you execute Engine.py directly.
    import numpy as np
    
    # A solvable test grid
    test_grid = np.array([
        [1, 8, 2],
        [0, 4, 3],
        [7, 6, 5]
    ])
    
    print("--- Running a direct test of Engine.py ---")
    print("Test Grid:\n", test_grid)
    
    solution = solve_puzzle(test_grid)
    
    if solution:
        print("\nSolution Found:")
        for i, step in enumerate(solution):
            print(f"Step {i+1}: {step}")
    else:
        print("\nNo solution found.")