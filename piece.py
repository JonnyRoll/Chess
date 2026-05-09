from os import remove

def capture_piece (opponent_set: set, killed_piece) -> None:
    opponent_set.remove(killed_piece)

class Piece:
    chess_board = [[0] * 8 for i in range(8)]
    black_player_pieces = set()
    white_player_pieces = set()
    def __init__(self, name:str ,vertical_axis:int, horizontal_axis:int, value:int, color:bool):
        self.name = name
        self.vertical_axis = vertical_axis
        self.horizontal_axis = horizontal_axis
        self.value = value
        self.color = color

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    def place_piece(self, vertical_desired:int, horizontal_desired:int) -> None:
        # removing the piece from old index
        Piece.chess_board[self.vertical_axis][self.horizontal_axis] = 0
        Piece.chess_board[vertical_desired][horizontal_desired] = self
        # updating the position values
        self.vertical_axis = vertical_desired
        self.horizontal_axis = horizontal_desired

    def valid_move_diagonal(self, vertical_direction: int, horizontal_direction: int) -> bool:
        if vertical_direction == 0 or horizontal_direction == 0:
            return False
        elif abs(vertical_direction) != abs(horizontal_direction):
            return False

        amount = abs(vertical_direction)
        for i in range(1,abs(vertical_direction)):
            if Piece.chess_board[self.vertical_axis + (i * (vertical_direction // abs(vertical_direction)))][self.horizontal_axis + (i * (horizontal_direction // abs(horizontal_direction)))] == 0:
                continue
            else: return False
        if Piece.chess_board[self.vertical_axis + (abs(amount) * (vertical_direction // abs(vertical_direction)))][self.horizontal_axis + (abs(amount) * (horizontal_direction // abs(horizontal_direction)))] == 0:
            return True
        elif Piece.chess_board[self.vertical_axis + (abs(amount) * (vertical_direction // abs(vertical_direction)))][self.horizontal_axis + (abs(amount) * (horizontal_direction // abs(horizontal_direction)))].color != self.color:
            opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
            vertical_index = self.vertical_axis + (abs(amount) * (vertical_direction // abs(vertical_direction)))
            horizontal_index = self.horizontal_axis + (abs(amount) * (horizontal_direction // abs(horizontal_direction)))
            capture_piece(opponent_set=opponent_pieces, killed_piece= Piece.chess_board[vertical_index][horizontal_index])
            return True
        else:
            return False


    # improve this to one path!
    def valid_move_vert_and_horz(self, amount: int, move_horizontally: bool) -> bool:
        if amount == 0:
            return False
        if move_horizontally:
            for i in range(1, abs(amount)):
                if Piece.chess_board[self.vertical_axis][self.horizontal_axis + (i * (amount // abs(amount)))] == 0:
                    continue
                else:
                    return False
            if Piece.chess_board[self.vertical_axis][self.horizontal_axis + amount] == 0:
                return True
            elif Piece.chess_board[self.vertical_axis][self.horizontal_axis + amount].color != self.color:
                # this will make the opponent_pieces variable black, if color is true (we are white), else opponent_pieces will be white (we are black)
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set = opponent_pieces, killed_piece = Piece.chess_board[self.vertical_axis][self.horizontal_axis + amount])
                return True
            else:
                return False

        else:
            for i in range(1, abs(amount)):
                if Piece.chess_board[self.vertical_axis + (i * (amount // abs(amount)))][self.horizontal_axis] == 0:
                    continue
                else:
                    return False
            if Piece.chess_board[self.vertical_axis + amount][self.horizontal_axis] == 0:
                return True
            elif Piece.chess_board[self.vertical_axis + amount][self.horizontal_axis].color != self.color:
                # remove peace from other player's list
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set = opponent_pieces, killed_piece = Piece.chess_board[self.vertical_axis + amount][self.horizontal_axis])
                return True
            else:
                return False

