import random
import time
GRID_ROWS = 3
GRID_COLS = 3
environment = {
    (r, c): random.randint(0, 1) 
    for r in range(GRID_ROWS) 
    for c in range(GRID_COLS)
}
location = (random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1))
print(f"--- Initial State ---")
print(f"Agent starts at: {location}")
for r in range(GRID_ROWS):
    print([environment[(r, c)] for c in range(GRID_COLS)])
print("-" * 25 + "\n")
for step in range(1, 31): # Increased steps for the larger environment
    print(f"--- Step {step} ---")
    time.sleep(0.5) # Pause for readability
    current_status = environment[location]
    print(f"Agent is at {location}. Status is {'Dirty' if current_status == 1 else 'Clean'}.")
    if current_status == 1: # If Dirty
        action = 'Suck'
        environment[location] = 0 # Clean the square
        print(f"Action: {action}. Cleaned {location}.")
    else: # If Clean, move to an adjacent square
        possible_moves = ['Up', 'Down', 'Left', 'Right']
        action = random.choice(possible_moves)
        row, col = location
        if action == 'Up':
            location = (max(0, row - 1), col)
        elif action == 'Down':
            location = (min(GRID_ROWS - 1, row + 1), col)
        elif action == 'Left':
            location = (row, max(0, col - 1))
        elif action == 'Right':
            location = (row, min(GRID_COLS - 1, col + 1))
        print(f"Action: Move {action}. New location: {location}")

    # Print the current state of the grid
    for r in range(GRID_ROWS):
        print([environment[(r, c)] for c in range(GRID_COLS)])
    print()

    # 4. CHECK if the goal state (all clean) has been reached
    if all(status == 0 for status in environment.values()):
        print("--- Goal State Reached: All rooms are clean! ---")
        break

