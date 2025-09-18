def play_tic_tac_toe():
    board = [' '] * 9
    player, computer = 'X', 'O'

    def print_board():
        print(f"\n|{board[0]}|{board[1]}|{board[2]}|")
        print(f"|{board[3]}|{board[4]}|{board[5]}|")
        print(f"|{board[6]}|{board[7]}|{board[8]}|")

    def check_win(b, p):
        # All possible winning combinations
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(b[i] == p for i in c) for c in win_conditions)

    def check_tie(b):
        return ' ' not in b

    print("Welcome to Tic-Tac-Toe!")
    while True:
        # Player's turn
        print_board()
        try:
            move = int(input(f"Player '{player}', enter your move (1-9): ")) - 1
            if not (0 <= move <= 8 and board[move] == ' '):
                print("Invalid move. Try again.")
                continue
            board[move] = player
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        # Check for player win or tie
        if check_win(board, player):
            print_board()
            print(f"Player '{player}' wins!")
            break
        if check_tie(board):
            print_board()
            print("It's a tie!")
            break

        # Computer's turn (find the first available spot)
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer
                break
        
        # Check for computer win or tie
        if check_win(board, computer):
            print_board()
            print(f"Computer '{computer}' wins!")
            break
        if check_tie(board):
            print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
