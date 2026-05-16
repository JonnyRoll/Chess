from Queen import Queen
from piece import Piece
from rook import Rook
from bishop import Bishop
from kight import Knight
from pawn import Pawn

def create_pieces(object:Piece) -> None:
    # this is the same as sating we will assign set de pending on how the colout (very clean!)
    player_set = Piece.white_player_pieces if object.color else Piece.black_player_pieces
    player_set.add(object)
    place_pieces_on_board(object)


def create_bishops() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Bishop(name='B1_W', vertical_axis=7, horizontal_axis=2, value=3))
    # if the piece has a color = true then it's a white piece
    create_pieces(Bishop(name='B2_W', vertical_axis=7, horizontal_axis=5, value=3))

    # if the piece has a color = false then it's a black piece
    create_pieces(Bishop(name='B1_B', vertical_axis=0, horizontal_axis=2, value=3))
    # if the piece has a color = false then it's a black piece
    create_pieces(Bishop(name='B2_B', vertical_axis=0, horizontal_axis=5, value=3))


def creat_rooks() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Rook(name='R1_W', vertical_axis=7, horizontal_axis=0, value=5))
    # if the piece has a color = true then it's a white piece
    create_pieces(Rook(name='R2_W', vertical_axis=7, horizontal_axis=7, value=5))


    # if the piece has a color = false then it's a black piece
    create_pieces(Rook(name='R1_B', vertical_axis=0, horizontal_axis=0, value=5))
    # if the piece has a color = false then it's a black piece
    create_pieces(Rook(name='R2_B', vertical_axis=0, horizontal_axis=7, value=5))


def creat_queens() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Queen(name='Q_W', vertical_axis=7, horizontal_axis=3, value=8))
    # if the piece has color = false then it is a black piece
    create_pieces(Queen(name='Q_B', vertical_axis=0, horizontal_axis=3, value=8))

def creat_knights() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Knight(name = 'K1_W', vertical_axis=7, horizontal_axis=1, value=3))
    create_pieces(Knight(name='K2_W', vertical_axis=7, horizontal_axis=6, value=3))

    # # if the piece has color = false then it is a black piece
    create_pieces(Knight(name = 'K1_B', vertical_axis=0, horizontal_axis=1, value=3))
    create_pieces(Knight(name = 'K2_B', vertical_axis=0, horizontal_axis=6, value=3))

def creat_pawn() -> None:
    for i in range(8):
        create_pieces(Pawn(name = f'P{i}_W', vertical_axis=6, horizontal_axis=i, value=1))
        create_pieces(Pawn(name = f'P{i}_B', vertical_axis=1, horizontal_axis=i, value=1))


# placing the chess pieces on the board!
def place_pieces_on_board(object:Piece) -> None:
    Piece.chess_board[object.vertical_axis][object.horizontal_axis] = object


def start_game() -> None:
    #creating pieces
    create_bishops()
    creat_rooks()
    creat_queens()
    creat_knights()
    creat_pawn()
    the_move_decide = True
    print_board()
    while(True):
        whose_moving_str = "It is whites tern to move!" if the_move_decide else "It is blacks tern to move!"
        print(whose_moving_str)
        the_move = input("What is your move? (uses spaces to separate), input R to resin: ")
        if the_move.upper() == "R":
            reside = 'White reside' if the_move_decide else 'Black reside'
            print(reside)
            break
        try:
            valid_move = move_piece(the_move[:-2].upper(), the_move[-2].upper(), int(the_move[-1].upper()))
            if valid_move:
                the_move_decide = not the_move_decide
                print("here is the new board")
                print_board()
            else:
                print("Invalid move!")
        except :
            print("that piece does not exist!")


def adjust_visual(element) -> None:
    if len(str(element)) == 1:
        print(f'  {element}  ', end= " ")
    elif len(str(element)) == 3:
        print(f' {element} ' , end= " ")
    elif len(str(element)) == 4:
        print(f' {element}', end= " ")
    else: print(element)


def print_board() -> None:
    for i in range (8):
        for j in range (8):
            adjust_visual(Piece.chess_board[i][j])
        print()


# this will map the input from move piece to the correct square on the board
def map_piece(horizontal_dirct:str, vertical_dirct:int) -> list:
    # mapping the vertical axis (making the top index 0 instead of 8)
    actual_vertical_index = abs(vertical_dirct - 8)
    # all valid horizontal inputs
    possible_horizontal_inputs = ['A','B','C','D','E','F','G','H']
    # the actual index we want the horizontal axis to be!
    actual_horizontal_index = 0

    # iterating threw in order to find the matching letter
    for letter in possible_horizontal_inputs:
        if letter == horizontal_dirct :
            # return the list of the correct indexes
            return [actual_vertical_index, actual_horizontal_index]
        # increments horizontal index (when letter inst matched)
        actual_horizontal_index += 1

    # in the case the horizontal direction char was not found
    return [999, 999]

# this will start with white (as it is always the first to move)
color_to_move = True
# this function will move the called on piece in the desired direction piece
def move_piece(piece_name: str,  horizontal_dirct:str, vertical_dirct:int) -> bool:
    #remap the input!
        # note the index [0] = ACTUAL_VERTICAL_INDEX and  index[1] = ACTUAL_HORIZONTAL_INDEX
    index_of_input = map_piece(horizontal_dirct = horizontal_dirct , vertical_dirct = vertical_dirct)
    # checks if the indexes return to use a valid for the board

    if 0 <= index_of_input[0] < 8 and 0 <= index_of_input[1] < 8:
        # this defines that we are using a global variable! (color_to_move)
        global color_to_move
        # Note true is when the piece is white, false when the piece is black
        piece_color = True if color_to_move else False
        piece_set = Piece.white_player_pieces if piece_color else Piece.black_player_pieces
        #finding the full name! (proud of this one)
        full_piece_name = f'{piece_name}_W' if color_to_move else f'{piece_name}_B'
        # flipping the to the other set (first switch is to black)
        color_to_move = not color_to_move
        # the piece is in the desired set!
        for piece in piece_set:
            # if we found the piece
            if piece.name == full_piece_name:
                # uses the specific move method for the particular piece!
                return piece.move(index_of_input[0], index_of_input[1])

    return False

# using this so that if we use game file on a different .py file we don't run the game again
if __name__ == "__main__":
    start_game()


















