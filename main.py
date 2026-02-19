# Global constant for the initial board state
# We use '1' through '9' as placeholders so the user knows which number to type.
INITIAL_BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_board(board):
    """ Prints the 3x3 game board to the console. """
    print("\n" + "—" * 13)
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---|---|---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---|---|---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("—" * 13 + "\n")


def check_win(board, player):
    """ Checks if the specified player has won the game. """
    # Define all 8 possible win conditions
    win_conditions = [
        # Horizontal rows
        (board[0] == player and board[1] == player and board[2] == player),
        (board[3] == player and board[4] == player and board[5] == player),
        (board[6] == player and board[7] == player and board[8] == player),
        # Vertical columns
        (board[0] == player and board[3] == player and board[6] == player),
        (board[1] == player and board[4] == player and board[7] == player),
        (board[2] == player and board[5] == player and board[8] == player),
        # Diagonals
        (board[0] == player and board[4] == player and board[8] == player),
        (board[2] == player and board[4] == player and board[6] == player)
    ]
    
    # The `any()` function returns True if any item in the list is True.
    return any(win_conditions)


def check_draw(board):
    """ Checks if the game is a draw (i.e., the board is full). """
    # A draw occurs if all spots are filled ('X' or 'O')
    # We can check if any of the original digit placeholders are left.
    for spot in board:
        if spot.isdigit():
            return False  # A spot is still available, not a draw
    return True  # No digit spots left, it's a draw


def get_player_move(board, player):
    """ Prompts the current player for their move and validates it. """
    while True:
        move_input = input(f"Player {player}, enter your move (1-9): ")
        
        try:
            move = int(move_input)
            if move in range(1, 10):
                index = move - 1  # Convert 1-9 to 0-8 index
                if board[index] in ['X', 'O']:
                    print("That spot is already taken! Please try again.")
                else:
                    return index 
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")


def main_game():
    print("Welcome to Tic-Tac-Toe!")
    
    # Create a copy of the initial board to play on
    board = INITIAL_BOARD[:]
    current_player = 'X'
    game_is_running = True
    
    while game_is_running:
        # Display the board at the start of each turn

        print_board(board)
        
        # Get the current player's move
        move_index = get_player_move(board, current_player)
        
        # Apply the move to the board
        board[move_index] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations, Player {current_player} wins!")
            game_is_running = False
        
        elif check_draw(board):
            print_board(board)
            print("The game is a draw!")
            game_is_running = False
            
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
                
    print("Thank you for playing!")


# This standard Python construct ensures that main_game()
# is called only when the script is executed directly.
if __name__ == "__main__":
    main_game()
