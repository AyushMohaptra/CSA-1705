# A Python program that implements the Minimax algorithm.

def minimax(node, depth, maximizing_player):
    """
    Implements the Minimax algorithm with no pruning.
    `node`: A list representing the game tree node.
    `depth`: The current depth in the tree.
    `maximizing_player`: Boolean, True if it's the maximizing player's turn.
    """

    # Base case: if the node is a leaf (a score), return its value.
    if not isinstance(node, list):
        return node

    if maximizing_player:
        best_value = -float('inf')
        for child in node:
            value = minimax(child, depth + 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node:
            value = minimax(child, depth + 1, True)
            best_value = min(best_value, value)
        return best_value

# A sample game tree with leaf nodes (scores) at the end.
# Positive scores are good for the maximizing player (first player).
game_tree = [[8, 4], [2, 6], [1, 9], [7, 3]]

# Find the best value for the starting player (maximizing player)
best_score = minimax(game_tree, 0, True)

print(f"The best possible score for the starting player is: {best_score}")
