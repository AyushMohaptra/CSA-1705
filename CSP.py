# A program to solve the Map Coloring problem using a backtracking CSP algorithm.

def solve_map_coloring():
    """
    Solves the map coloring problem for a predefined graph using backtracking.
    """
    # 1. Define the variables (map regions)
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    
    # 2. Define the domains (available colors)
    colors = ['red', 'green', 'blue']
    
    # 3. Define the constraints (adjacency)
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }
    
    # The backtracking function
    def backtrack(assignment):
        # Base case: if all variables are assigned, a solution is found.
        if len(assignment) == len(variables):
            return assignment
        
        # Select the next unassigned variable.
        unassigned = next(v for v in variables if v not in assignment)
        
        # Try each color from the domain.
        for color in colors:
            # Check if the color is consistent with neighboring assignments.
            if all(neighbors[unassigned]):
              if all(assignment.get(neighbor) != color for neighbor in neighbors[unassigned]):
                  assignment[unassigned] = color
                  # Recursively search for a solution.
                  result = backtrack(assignment)
                  if result:
                      return result
            
        # Backtrack if no valid color is found.
        return None

    return backtrack({})

if __name__ == "__main__":
    solution = solve_map_coloring()
    if solution:
        print("Map Coloring Solution Found:")
        for state, color in solution.items():
            print(f"{state}: {color}")
    else:
        print("No solution found.")
