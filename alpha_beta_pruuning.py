# A Python program that implements the Minimax algorithm with Alpha-Beta Pruning.

def minimax_with_pruning(node, depth, alpha, beta, maximizing_player):
    """
    Implements the Minimax algorithm with Alpha-Beta pruning.
    `node`: A list representing the game tree node or a numerical score.
    `depth`: The current depth in the tree.
    `alpha`: The best value found so far for the maximizing player.
    `beta`: The best value found so far for the minimizing player.
    `maximizing_player`: Boolean, True if it's the maximizing player's turn.
    """
    # Base case: if the node is a leaf (a score), return its value.
    if not isinstance(node, list):
        return node

    if maximizing_player:
        best_value = -float('inf')
        for child in node:
            value = minimax_with_pruning(child, depth + 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cut-off (pruning)
        return best_value
    else:  # Minimizing player
        best_value = float('inf')
        for child in node:
            value = minimax_with_pruning(child, depth + 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Alpha cut-off (pruning)
        return best_value

# A sample game tree with leaf nodes (scores) at the end.
# Positive scores are good for the maximizing player.
game_tree = [[8, 4], [2, 6], [1, 9], [7, 3]]

# Find the best value for the starting player (maximizing player)
best_score = minimax_with_pruning(game_tree, 0, -float('inf'), float('inf'), True)

print(f"The best possible score for the starting player is: {best_score}")
