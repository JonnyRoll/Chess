from piece import Piece
from rook import Rook
from bishop import Bishop

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



# placing the chess pieces on the board!
def place_pieces_on_board(object:Piece) -> None:
    Piece.chess_board[object.vertical_axis][object.horizontal_axis] = object


def start_game() -> None:
    #creating pieaces
    create_bishops()
    creat_rooks()



def print_board() -> None:
    for i in range (8):
        print(Piece.chess_board[i])


start_game()
print_board()












