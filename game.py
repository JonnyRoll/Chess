from Queen import Queen
from piece import Piece
from rook import Rook
from bishop import Bishop
from kight import Kight

def create_pieces(object:Piece) -> None:
    # this is the same as sating we will assign set de  penfing on how the colout (very clean!)
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
    # if the piece has a color = false then its a black piece
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
    create_pieces(Kight(name = 'K1_W', vertical_axis=7, horizontal_axis=1, value=3, color=True))
    create_pieces(Kight(name='K2_W', vertical_axis=7, horizontal_axis=6, value=3, color=True))

    # # if the piece has color = false then it is a black piece
    create_pieces(Kight(name = 'K1_B', vertical_axis=0, horizontal_axis=1, value=3, color=False))
    create_pieces(Kight(name = 'K2_B', vertical_axis=0, horizontal_axis=6, value=3, color=False))


# placing the chess pieces on the board!
def place_pieces_on_board(object:Piece) -> None:
    Piece.chess_board[object.vertical_axis][object.horizontal_axis] = object


def start_game() -> None:
    #creating pieces
    create_bishops()
    creat_rooks()
    creat_queens()
    creat_knights()


def print_board() -> None:
    for i in range (8):
        print(Piece.chess_board[i])

# this function will move the called on piece in the desired direction piece
def move_piece(vertical_dirct:int, horizontal_dirct:int, piece_color: bool, piece_name: str) -> bool:
    piece_set = Piece.white_player_pieces if piece_color else Piece.black_player_pieces
    # the piece is in the desired set!
    for piece in piece_set:
        # if we found the piece
        if piece.name == piece_name:
            # uses the specific move method for the particular piece!
            return piece.move(vertical_dirct, horizontal_dirct)

    else: return False




start_game()
print_board()
move_piece(2,2,False,'B1_B')
move_piece(-3,-3,True,'B2_W')
move_piece(-2,2,True,'B2_W')
move_piece(2,1, False,'K1_B')

print()
print()
print_board()
print('white pieces:', Piece.white_player_pieces)
print('black pieces:', Piece.black_player_pieces)













