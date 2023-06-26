
# Tic Tac Toe Game ----- Kumar Prince

board = [' ' for _ in range(9)]

def display_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# check if the board is full
def check_full():
    return ' ' not in board

def play_game():
    current_player = 'X'

    while True:
        display_board()


        print("Player", current_player, "turn.")
        move = int(input("Enter a position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = current_player

        if check_win(current_player):
            display_board()
            print("Player", current_player, "wins!")
            break

        # Check for a tie
        if check_full():
            display_board()
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
