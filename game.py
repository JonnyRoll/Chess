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
    create_pieces(Bishop(name='B1_W', vertical_axis=7, horizontal_axis=2, value=3, color=True))
    # if the piece has a color = true then it's a white piece
    create_pieces(Bishop(name='B2_W', vertical_axis=7, horizontal_axis=5, value=3, color=True))

    # if the piece has a color = false then it's a black piece
    create_pieces(Bishop(name='B1_B', vertical_axis=0, horizontal_axis=2, value=3, color=False))
    # if the piece has a color = false then it's a black piece
    create_pieces(Bishop(name='B2_B', vertical_axis=0, horizontal_axis=5, value=3, color=False))


def creat_rooks() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Rook(name='R1_W', vertical_axis=7, horizontal_axis=0, value=5, color=True))
    # if the piece has a color = true then it's a white piece
    create_pieces(Rook(name='R2_W', vertical_axis=7, horizontal_axis=7, value=5, color=True))


    # if the piece has a color = false then it's a black piece
    create_pieces(Rook(name='R1_B', vertical_axis=0, horizontal_axis=0, value=5, color=False))
    # if the piece has a color = false then it's a black piece
    create_pieces(Rook(name='R2_B', vertical_axis=0, horizontal_axis=7, value=5, color=False))


def creat_queens() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Queen(name='Q_W', vertical_axis=7, horizontal_axis=3, value=8, color=True))
    # if the piece has color = false then it is a black piece
    create_pieces(Queen(name='Q_B', vertical_axis=0, horizontal_axis=3, value=8, color=False))

def creat_knights() -> None:
    # if the piece has a color = true then it's a white piece
    create_pieces(Knight(name = 'K1_W', vertical_axis=7, horizontal_axis=1, value=3, color=True))
    create_pieces(Knight(name='K2_W', vertical_axis=7, horizontal_axis=6, value=3, color=True))

    # # if the piece has color = false then it is a black piece
    create_pieces(Knight(name = 'K1_B', vertical_axis=0, horizontal_axis=1, value=3, color=False))
    create_pieces(Knight(name = 'K2_B', vertical_axis=0, horizontal_axis=6, value=3, color=False))

def creat_pawn() -> None:
    for i in range(8):
        create_pieces(Pawn(name = f'P{i}_W', vertical_axis=6, horizontal_axis=i, value=1, color=True))
        create_pieces(Pawn(name = f'P{i}_B', vertical_axis=1, horizontal_axis=i, value=1, color=False))


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
    possible_horizontal_inputs = ['a','b','c','d','e','f','g','h']
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


# this function will move the called on piece in the desired direction piece
def move_piece(piece_name: str,  horizontal_dirct:str, vertical_dirct:int, piece_color: bool) -> bool:
    #remap the input!
        # note the index [0] = ACTUAL_VERTICAL_INDEX and  index[1] = ACTUAL_HORIZONTAL_INDEX
    index_of_input = map_piece(horizontal_dirct = horizontal_dirct , vertical_dirct = vertical_dirct)
    # checks if the indexes return to use a valid for the board
    if 0 <= index_of_input[0] < 8 and 0 <= index_of_input[1] < 8:
        print(index_of_input)
        piece_set = Piece.white_player_pieces if piece_color else Piece.black_player_pieces
        # the piece is in the desired set!
        for piece in piece_set:
            # if we found the piece
            if piece.name == piece_name:
                # uses the specific move method for the particular piece!
                return piece.move(index_of_input[0], index_of_input[1])

    return False

start_game()
print_board()
move_piece('K1_B','c',6,False)



print()
print()
print_board()
print()
print()
print('white pieces:', Piece.white_player_pieces)
print('black pieces:', Piece.black_player_pieces)
















