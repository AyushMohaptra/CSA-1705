def solve(board, col):
    if col >= 8:
        # A solution is found, print it and stop.
        for row in range(8):
            print(" ".join("Q" if board[col] == row else "." for col in range(8)))
        return True

    for row in range(8):
        # Check safety: No queen in same row or diagonal in previous columns.
        if all(row != board[i] and abs(row - board[i]) != col - i for i in range(col)):
            board[col] = row # Place queen
            if solve(board, col + 1):
                return True # If a solution is found by the recursive call, exit.
    
    return False

# Start the solver for an 8x8 board from the first column (0).
solve([-1] * 8, 0)

