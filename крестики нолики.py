import random
def draw_board(board):
    print("---------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n---------")
def get_player_move(board):
    while True:
        row = int(input("Введите номер строки (1, 2, 3): "))
        col = int(input("Введите номер столбца (1, 2, 3): "))
        if board[row-1][col-1] == "-":
            return row-1, col-1
        print("Неверный ход. Попробуйте еще раз.")
def get_computer_move(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                empty_cells.append((i, j))
    return random.choice(empty_cells)
def check_winner(board, player):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def play_game():
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]
    player = "X"  
    computer = "O"
    while True:
        draw_board(board)
        if player == "X":
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
            print("Компьютер выбрал ход: {}".format((row+1, col+1)))
        board[row][col] = player
        if check_winner(board, player):
            draw_board(board)
            print("Победитель: {}".format(player))
            break
        if "-" not in [cell for row in board for cell in row]:
            draw_board(board)
            print("Ничья!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

play_game()
