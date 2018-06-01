#### A game of Tic Tac Toe
#### command line-based version

import sys

# game essentials
BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
PLAYER = "X"
ROWS = ["a", "b", "c"]

def draw_board():
    board_string = "   1 2 3\n"
    row_index = 0
    for row in BOARD:
        row_string = ROWS[row_index] + " |"
        for cell in row:
            row_string += cell + "|"
        board_string += row_string + "\n"
        row_index += 1
    print(board_string)

def cell_is_empty(cell):
    row = ROWS.index(cell[0])
    column = int(cell[1])-1
    return BOARD[row][column] == " "

def input_is_valid(user_input):
    return len(user_input) == 2\
           and user_input[0] in ROWS\
           and user_input[1] in "123"

def get_user_input():
    print("Which cell do you want to fill?")
    while True:
        user_input = input()
        if not input_is_valid(user_input):
            print("You entered an invalid cell name. Try again!")
        elif not cell_is_empty(user_input):
            print("The cell you entered is not empty. Try again!")
        else:
            return user_input
            break

def fill_cell(cell):
    global BOARD
    row = ROWS.index(cell[0])
    column = int(cell[1])-1
    BOARD[row][column] = PLAYER

def take_turn():
    global PLAYER
    print("It's " + PLAYER + "'s turn.")
    cell = get_user_input()
    fill_cell(cell)
    if PLAYER == "X":
        PLAYER = "O"
    else:
        PLAYER = "X"

def reset():
    global BOARD, PLAYER
    PLAYER = "X"
    for row in BOARD:
        for cell in range(len(row)):
            row[cell] = " "

def play():
    print("\nWelcome to the game!")
    print("We start with an empty board.")
    draw_board()
    for number_of_cells in range(9):
        take_turn()
        print("This is the current state of the game:")
        draw_board()
    if play_again():
        reset()
        play()
    else:
        sys.exit()

def play_again():
    print("Thank you for playing! Do you want to play again? (y/n)")
    while True:
        play_again = input()
        if play_again not in "yn":
            print("Sorry, didn't quite catch that. Please enter 'y' or 'n'.")
        else:
            return play_again.lower().startswith("y")

play()

