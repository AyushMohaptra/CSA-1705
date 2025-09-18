import heapq

class Node:
    def __init__(self, mat, x, y, level, parent):
        self.mat = mat
        self.x = x
        self.y = y
        self.level = level
        self.parent = parent
        self.cost = 0

    def __lt__(self, other):
        return (self.cost + self.level) < (other.cost + other.level)

def calculate_cost(mat, goal):
    return sum(1 for i in range(3) for j in range(3) if mat[i][j] != 0 and mat[i][j] != goal[i][j])

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def print_path(node):
    path = []
    while node:
        path.append(node.mat)
        node = node.parent
    for mat in reversed(path):
        for row in mat:
            print(' '.join(map(str, row)))
        print()

def solve(initial, x, y, goal):
    moves = [(1,0), (0,-1), (-1,0), (0,1)]
    root = Node(initial, x, y, 0, None)
    root.cost = calculate_cost(initial, goal)
    heap = [root]

    visited = set()
    while heap:
        node = heapq.heappop(heap)
        state_tuple = tuple(tuple(row) for row in node.mat)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        # Print the current step
        print(f"Step {node.level}:")
        for row in node.mat:
            print(' '.join(map(str, row)))
        print()
        # Check if goal is reached
        if node.cost == 0:
            print("Goal reached!\nPath:")
            print_path(node)
            return
        for dx, dy in moves:
            nx, ny = node.x + dx, node.y + dy
            if is_valid(nx, ny):
                new_mat = [row[:] for row in node.mat]
                new_mat[node.x][node.y], new_mat[nx][ny] = new_mat[nx][ny], new_mat[node.x][node.y]
                child_tuple = tuple(tuple(row) for row in new_mat)
                if child_tuple not in visited:
                    child = Node(new_mat, nx, ny, node.level + 1, node)
                    child.cost = calculate_cost(new_mat, goal)
                    heapq.heappush(heap, child)


initial_input = list(map(int, input("Enter the initial state (9 space-separated numbers, use 0 for blank): ").split()))
if len(initial_input) != 9:
    print("Error: Please enter exactly 9 numbers.")
    exit(1)
if 0 not in initial_input:
    print("Error: Input must contain a 0 to represent the blank space.")
    exit(1)
initial = [initial_input[i*3:(i+1)*3] for i in range(3)]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# Find the position of 0 (blank)
x = y = None
for i in range(3):
    for j in range(3):
        if initial[i][j] == 0:
            x, y = i, j
if x is None or y is None:
    print("Error: Could not find blank (0) in the input.")
    exit(1)
solve(initial, x, y, goal)





