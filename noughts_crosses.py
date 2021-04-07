# Noughts and Crosses (console) v2
# featuring computer opponent

import random


def print_board(board):
    """The print_board(board) function prints the current board to the command window. Returns True on completion."""
    print("\n ", board[1], " | ", board[2], " | ", board[3])
    print("-----+-----+-----")
    print(" ", board[4], " | ", board[5], " | ", board[6])
    print("-----+-----+-----")
    print(" ", board[7], " | ", board[8], " | ", board[9])
    return True


def update_board(board, position, marker):
    """The update_board(board, position, marker) function returns the updated board once a move has been made."""
    board[position] = marker
    print_board(board)
    return board


def check_winner(board, markers, turn_selector):
    """The check_winner(board, markers, turn_selector) function checks for a win condition. Prints to console on win or draw.
    Returns marker for win, True for draw, False to continue game."""
    for marker in markers:
        # top row, middle row, bottom row
        # first column, second column, third column
        # diagonal, top left to bottom right & diagonal, top right to bottom left
        if ( board[1] == marker and board[2] == marker and board[3] == marker ) or \
        ( board[4] == marker and board[5] == marker and board[6] == marker ) or \
        ( board[7] == marker and board[8] == marker and board[9] == marker ) or \
        ( board[1] == marker and board[4] == marker and board[7] == marker ) or \
        ( board[2] == marker and board[5] == marker and board[8] == marker ) or \
        ( board[3] == marker and board[6] == marker and board[9] == marker ) or \
        ( board[1] == marker and board[5] == marker and board[9] == marker ) or \
        ( board[3] == marker and board[5] == marker and board[7] == marker ):
            print("\n=====================\n Player " + str(turn_selector + 1) + "(" + str(marker) + ") has won!\n=====================\n")
            return marker
    # If all locations are filled, game is a draw - have to check after win
    if " " not in board:
        print("\n=====================\n The game is a draw!\n=====================\n")
        return True
    return False    


def make_a_move(board, markers, turn_selector): 
    """The make_a_move(board, markers, turn_selector) function takes input from user and ensures the chosen location is empty.
    Returns position to play (1-9)."""
    marker = markers[turn_selector]
    while True:
        try:
            position_to_play = int(input("\nPlayer " + str(turn_selector + 1) + " (" + str(marker) + \
            ") to play. Where would you like to place your marker? ").strip())
            if position_to_play >= 1 and position_to_play <= 9:
                if board[position_to_play] == " ":
                    break
                else:
                    print("That location is occupied, please choose a new location.")
            else:
                print("That is not a valid location! Must be a number between 1-9 and an unoccupied position.")
        except:
            print("That is not a valid location! Must be a number between 1-9 and an unoccupied position.")
    return position_to_play


def choose_first_marker():
    """The choose_first_marker() function takes input on xo or ox order of play. Returns chosen order in a list - index 0 and 1."""
    while True:
        try:
            marker_to_play_first = input("Which marker should play first? x or o: ").lower().strip()
            if marker_to_play_first == "x":
                return ["x", "o"]
            elif marker_to_play_first == "o":
                return ["o", "x"]
        except:
            print("Erroneous input.\n")        
        print("Please input either x or o.\n")


def choose_option(text, responses):
    """The choose_option(text, responses) function gives a question to the user and offers 2 answers.
    Pass question in as text. Responses should be list, index 0 and 1. 0 response returns True, 1 response returns False."""
    while True:
        try:
            user_answer = input(text + " " + str(responses[0].upper()) + "/" + str(responses[1].upper()) + ": ").lower().strip()
            if user_answer == responses[0]:
                return True
            elif user_answer == responses[1]:
                return False
        except:
            print("Erroneous input.\n")
        print("Please input either " + str(responses[0].upper()) + " or " + str(responses[1].upper()) + ".\n")


def switch_markers(markers):
    """The switch_markers(markers) function returns the opposite version of the markers list."""
    if markers == ["x","o"]:
        return ["o","x"]
    else:
        return ["x","o"]


def move_piece(board, markers, turn_selector):
    """The move_piece(board, markers, turn_selector) function validates moving the player's selected marker to an empty position.
    Returns True on completion."""
    while True:
        try:
            start_location = int(input("Which marker would you like to move? 1-9: ").strip())
            if start_location >= 1 or start_location <= 9:
                if board[start_location] == markers[turn_selector]:
                    break
                else:
                    print("You're playing as " + str(markers[turn_selector]) + ". You can't move a " + str(markers[(turn_selector + 1) % 2]) + "marker.")
            else:
                print("That is not a valid location! Number must be between 1-9 and have your marker occupying that location.")
        except:
            print("That is not a valid location! Number must be between 1-9 and have your marker occupying that location.")

    marker_to_move = board[start_location]

    while True:
        try:
            end_location = int(input("Where would you like to move the marker to? 1-9: ").strip())
            if end_location >= 1 or end_location <= 9:
                if board[end_location] == " ":
                    break
                else:
                    print("You must choose an empty position.")
            else:
                print("That is not a valid location! Number must be between 1-9.")
        except:
            print("That is not a valid location! Number must be between 1-9.")

    update_board(board, start_location, " ")
    update_board(board, end_location, marker_to_move)
    return True


def check_marker_on_board(board, markers, turn_selector):
    """The check_marker_on_board(board, markers, turn_selector) function returns True if the current player's marker is present at least once on the board."""
    for i in range(9):
        if board[i] == markers[turn_selector]:
            return True
    return False
    

def computer_to_move(board, markers, turns_counter):
    """The computer_to_move(board, markers, turns_counter) function makes the smart decision for the computer's move.
    Returns True on completion."""
    # respond to a centre play with a corner play
    # respond to corner with a centre
    # respond to edge opener with center or corner next to x (in our case, computer will always pick centre) 
    position_to_play = 1
    if turns_counter <= 2:
        # Centre play
        if board[5] == " ":
            position_to_play = 5
        else:
            # Randomise the corner to chose
            positions_to_chose_from = [1, 3, 7, 9]
            position_to_play = positions_to_chose_from[random.randint(0,3)]
    else:
        # OFFENSIVE - done before defensive so computer tries to win before trying to draw
        # top row
        if ( board[1] == markers[1] and board[2] == markers[1] and board[3] == " " ):
            position_to_play = 3
        elif ( board[1] == markers[1] and board[2] == " " and board[3] == markers[1] ):
            position_to_play = 2
        elif ( board[1] == " " and board[2] == markers[1] and board[3] == markers[1] ):
            position_to_play = 1
        # middle row
        elif ( board[4] == markers[1] and board[5] == markers[1] and board[6] == " " ):
            position_to_play = 6
        elif ( board[4] == markers[1] and board[5] == " " and board[6] == markers[1] ):
            position_to_play = 5
        elif ( board[4] == " " and board[5] == markers[1] and board[6] == markers[1] ):
            position_to_play = 4
        # bottom row
        elif ( board[7] == markers[1] and board[8] == markers[1] and board[9] == " " ):
            position_to_play = 9
        elif ( board[7] == markers[1] and board[8] == " " and board[9] == markers[1] ):
            position_to_play = 8
        elif ( board[7] == " " and board[8] == markers[1] and board[9] == markers[1] ):
            position_to_play = 7
        # first column
        elif ( board[1] == markers[1] and board[4] == markers[1] and board[7] == " " ):
            position_to_play = 7
        elif ( board[1] == markers[1] and board[4] == " " and board[7] == markers[1] ):
            position_to_play = 4
        elif ( board[1] == " " and board[4] == markers[1] and board[7] == markers[1] ):
            position_to_play = 1
        # second column
        elif ( board[2] == markers[1] and board[5] == markers[1] and board[8] == " " ):
            position_to_play = 8
        elif ( board[2] == markers[1] and board[5] == " " and board[8] == markers[1] ):
            position_to_play = 5
        elif ( board[2] == " " and board[5] == markers[1] and board[8] == markers[1] ):
            position_to_play = 2
        # third column
        elif ( board[3] == markers[1] and board[6] == markers[1] and board[9] == " " ):
            position_to_play = 9
        elif ( board[3] == markers[1] and board[6] == " " and board[9] == markers[1] ):
            position_to_play = 6
        elif ( board[3] == " " and board[6] == markers[1] and board[9] == markers[1] ):
            position_to_play = 3
        # diagonal, top left to bottom right
        elif ( board[1] == markers[1] and board[5] == markers[1] and board[9] == " " ):
            position_to_play = 7
        elif ( board[1] == markers[1] and board[5] == " " and board[9] == markers[1] ):
            position_to_play = 5
        elif ( board[1] == " " and board[5] == markers[1] and board[9] == markers[1] ):
            position_to_play = 1
        # diagonal, top right to bottom left
        elif ( board[3] == markers[1] and board[5] == markers[1] and board[7] == " " ):
            position_to_play = 7
        elif ( board[3] == markers[1] and board[5] == " " and board[7] == markers[1] ):
            position_to_play = 5
        elif ( board[3] == " " and board[5] == markers[1] and board[7] == markers[1] ):
            position_to_play = 3

        # BLOCK ANY BRANCHES - check corners and the location in an L shape from this, typical branch, block on branch side
        # top left corner
        elif ( board[1] == markers[0] and board[6] == markers[0] and turns_counter <=4 ):
            position_to_play = 3
        elif ( board[1] == markers[0] and board[8] == markers[0] and turns_counter <=4 ):
            position_to_play = 7
        # top right corner
        elif ( board[3] == markers[0] and board[4] == markers[0] and turns_counter <=4 ):
            position_to_play = 1
        elif ( board[3] == markers[0] and board[8] == markers[0] and turns_counter <=4 ):
            position_to_play = 9
        # bottom left corner
        elif ( board[7] == markers[0] and board[2] == markers[0] and turns_counter <=4 ):
            position_to_play = 1
        elif ( board[7] == markers[0] and board[6] == markers[0] and turns_counter <=4 ):
            position_to_play = 9
        # bottom right corner
        elif ( board[9] == markers[0] and board[2] == markers[0] and turns_counter <=4 ):
            position_to_play = 3
        elif ( board[9] == markers[0] and board[4] == markers[0] and turns_counter <=4 ):
            position_to_play = 7

        # BLOCK three corner play
        elif ( board[1] == markers[0] and board[5] == markers[1] and board[9] == markers[0] and turns_counter <=4 ):
            # Randomise the location to chose
            positions_to_chose_from = [2, 4, 6, 8]
            position_to_play = positions_to_chose_from[random.randint(0,3)]
        elif ( board[7] == markers[0] and board[5] == markers[1] and board[3] == markers[0] and turns_counter <=4 ):
            # Randomise the location to chose
            positions_to_chose_from = [2, 4, 6, 8]
            position_to_play = positions_to_chose_from[random.randint(0,3)]

        # DEFENSIVE
        # top row
        elif ( board[1] == markers[0] and board[2] == markers[0] and board[3] == " " ):
            position_to_play = 3
        elif ( board[1] == markers[0] and board[2] == " " and board[3] == markers[0] ):
            position_to_play = 2
        elif ( board[1] == " " and board[2] == markers[0] and board[3] == markers[0] ):
            position_to_play = 1
        # middle row
        elif ( board[4] == markers[0] and board[5] == markers[0] and board[6] == " " ):
            position_to_play = 6
        elif ( board[4] == markers[0] and board[5] == " " and board[6] == markers[0] ):
            position_to_play = 5
        elif ( board[4] == " " and board[5] == markers[0] and board[6] == markers[0] ):
            position_to_play = 4
        # bottom row
        elif ( board[7] == markers[0] and board[8] == markers[0] and board[9] == " " ):
            position_to_play = 9
        elif ( board[7] == markers[0] and board[8] == " " and board[9] == markers[0] ):
            position_to_play = 8
        elif ( board[7] == " " and board[8] == markers[0] and board[9] == markers[0] ):
            position_to_play = 7
        # first column
        elif ( board[1] == markers[0] and board[4] == markers[0] and board[7] == " " ):
            position_to_play = 7
        elif ( board[1] == markers[0] and board[4] == " " and board[7] == markers[0] ):
            position_to_play = 4
        elif ( board[1] == " " and board[4] == markers[0] and board[7] == markers[0] ):
            position_to_play = 1
        # second column
        elif ( board[2] == markers[0] and board[5] == markers[0] and board[8] == " " ):
            position_to_play = 8
        elif ( board[2] == markers[0] and board[5] == " " and board[8] == markers[0] ):
            position_to_play = 5
        elif ( board[2] == " " and board[5] == markers[0] and board[8] == markers[0] ):
            position_to_play = 2
        # third column
        elif ( board[3] == markers[0] and board[6] == markers[0] and board[9] == " " ):
            position_to_play = 9
        elif ( board[3] == markers[0] and board[6] == " " and board[9] == markers[0] ):
            position_to_play = 6
        elif ( board[3] == " " and board[6] == markers[0] and board[9] == markers[0] ):
            position_to_play = 3
        # diagonal, top left to bottom right
        elif ( board[1] == markers[0] and board[5] == markers[0] and board[9] == " " ):
            position_to_play = 9
        elif ( board[1] == markers[0] and board[5] == " " and board[9] == markers[0] ):
            position_to_play = 5
        elif ( board[1] == " " and board[5] == markers[0] and board[9] == markers[0] ):
            position_to_play = 1
        # diagonal, top right to bottom left
        elif ( board[3] == markers[0] and board[5] == markers[0] and board[7] == " " ):
            position_to_play = 7
        elif ( board[3] == markers[0] and board[5] == " " and board[7] == markers[0] ):
            position_to_play = 5
        elif ( board[3] == " " and board[5] == markers[0] and board[7] == markers[0] ):
            position_to_play = 3       

    while True:
        if board[position_to_play] == " ":
            break
        else:
            # Backup incase above logic fails, ensures comptuer doesn't overwrite another marker
            position_to_play = random.randint(1,9)

    print("\nComputer's move: ")
    update_board(board, position_to_play, markers[1])
    return True


board       = [False, " ", " ", " ", " ", " ", " ", " ", " ", " "]
position    = [False, '1', '2', '3', '4', '5', '6', '7', '8', '9']
markers     = ["x","o"] # only for default order - not to change markers usable in game
turns_counter = 1
turn_selector = 0

# Assign Boolean values to gameplay options
gameplay_computer_opponent  = choose_option("Do you want to play against the computer?" , ["y","n"])
gameplay_both_markers       = choose_option("Do you want to be able to play as either X or O on your turns?", ["y","n"])
gameplay_move_pieces        = choose_option("Do you want to be able to move already placed markers?", ["y","n"])
if gameplay_both_markers == False:
    # Chose if player 1 is x or o
    markers = choose_first_marker()

print_board(board)
print_board(position)

# Main loop
while True:
    # Player move
    if (gameplay_computer_opponent == False) or (gameplay_computer_opponent and turn_selector == 0 ):  
        if gameplay_both_markers:
            print("\nPlayer " + str(turn_selector + 1) + " to play.")
            if choose_option("Do you want to play as X or O for this move?", ["x","o"]): # player wants x
                markers[turn_selector] = "x"
                markers[(turn_selector + 1) % 2] = "o"
            else: # player wants o
                markers[turn_selector] = "o"
                markers[(turn_selector + 1) % 2] = "x"

        # Check if there is a marker on the board to move (and player wants to move a piece), otherwise skip moving option
        if gameplay_move_pieces and check_marker_on_board(board, markers, turn_selector) and \
        choose_option("Do you want to move a marker (Y) or place a new marker (N) this turn?", ["y","n"]):
            move_piece(board, markers, turn_selector)
        else:
            update_board(board, make_a_move(board, markers, turn_selector), markers[turn_selector])
    # Computer move
    else:  
        computer_to_move(board, markers, turns_counter)

    # Check for a win
    if check_winner(board, markers, turn_selector) != False:
        break

    # Switch between 0 and 1
    turn_selector = (turn_selector + 1) % 2
    turns_counter = turns_counter + 1

exit()