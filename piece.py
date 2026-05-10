# this is the abstract method library!
from abc import ABC, abstractmethod

def capture_piece (opponent_set: set, killed_piece) -> None:
    opponent_set.remove(killed_piece)

# the ABC says that this is a abstract class (cannot make an instance of it!), can only makes instance of its children
class Piece(ABC):
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

    # this is the abstract method!
    @abstractmethod
    def move(self, vertical_direction: int, horizontal_direction: int):
        pass

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

    def valid_knight_move(self, vertical_direction: int, horizontal_direction: int) -> bool:
        new_vertical = self.vertical_axis + vertical_direction
        new_horizontal = self.horizontal_axis + horizontal_direction
        # in the case that 0,0 is entered (not a move) or if the move does not make sense for a knight
        if vertical_direction == 0 or horizontal_direction == 0:
            return False

        elif ((abs(vertical_direction) != 2 or abs(horizontal_direction) != 1)
              and
              (abs(vertical_direction) != 1 or abs(horizontal_direction) != 2)) :
            return False


        # if the position on the board would be invalid (using De Morgan law!) not (p and  q) = (not p) or (not q)
        elif not ((0 <= new_vertical < 8) and  (0<= new_horizontal < 8)):
            return False

        # the user entered a valid number!
        else:

            # the position is empty on the board
            if Piece.chess_board[new_vertical][new_horizontal] == 0:
                return True
            # the position is filled by an opponent piece (need to remove it)
            elif Piece.chess_board[new_vertical][new_horizontal].color != self.color:
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                vertical_index = new_vertical
                horizontal_index = new_horizontal
                capture_piece(opponent_set=opponent_pieces, killed_piece=Piece.chess_board[vertical_index][horizontal_index])
                return True
            # the position is filled by a piece from the same team (color)
            else:
                return False



