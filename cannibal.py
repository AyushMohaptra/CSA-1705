from collections import deque

# A simple class to represent the state (missionaries, cannibals, boat_side)
class State:
    def __init__(self, m, c, b):
        self.m = m  # Missionaries on the left bank
        self.c = c  # Cannibals on the left bank
        self.b = b  # Boat side (1=left, 0=right)
        self.parent = None

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __hash__(self):
        return hash((self.m, self.c, self.b))

    def is_valid(self):
        # Check for invalid number of people
        if not (0 <= self.m <= 3 and 0 <= self.c <= 3):
            return False
        # Check if cannibals outnumber missionaries on either bank
        if (self.m > 0 and self.m < self.c) or \
           (3 - self.m > 0 and 3 - self.m < 3 - self.c):
            return False
        return True

def solve():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)
    queue = deque([initial_state])
    visited = {initial_state}
    
    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return reversed(path)

        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # M, C
        for move_m, move_c in moves:
            if current_state.b == 1:  # Boat is on the left side
                new_state = State(current_state.m - move_m, current_state.c - move_c, 0)
            else:  # Boat is on the right side
                new_state = State(current_state.m + move_m, current_state.c + move_c, 1)

            if new_state.is_valid() and new_state not in visited:
                new_state.parent = current_state
                queue.append(new_state)
                visited.add(new_state)
    return None

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Path to solve the Missionaries and Cannibals problem:")
        for state in solution:
            print(f"({state.m} missionaries, {state.c} cannibals, boat on {'left' if state.b == 1 else 'right'} bank)")
    else:
        print("No solution found.")
