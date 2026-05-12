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
    def move(self, vertical_destination_int: int, horizontal_destination_letter: int):
        pass

    def place_piece(self, vertical_desired:int, horizontal_desired:int) -> None:
        # removing the piece from old index
        Piece.chess_board[self.vertical_axis][self.horizontal_axis] = 0
        Piece.chess_board[vertical_desired][horizontal_desired] = self
        # updating the position values
        self.vertical_axis = vertical_desired
        self.horizontal_axis = horizontal_desired

    def valid_move_diagonal(self, vertical_destination: int, horizontal_destination: int) -> bool:
        amount_moved_vertical = vertical_destination - self.vertical_axis
        amount_moved_horizontal = horizontal_destination - self.horizontal_axis
        # if we do not move from at least 1 axis
        if amount_moved_vertical== 0 or amount_moved_horizontal == 0:
            return False
        # if both axis don't move the same amount
        elif abs(amount_moved_vertical) != abs(amount_moved_horizontal):
            return False

        vertical_direction = amount_moved_vertical // abs(amount_moved_vertical)
        horizontal_direction = amount_moved_horizontal // abs(amount_moved_horizontal)
        for i in range(1, abs(amount_moved_vertical)):
            if Piece.chess_board[self.vertical_axis + (i * vertical_direction)][self.horizontal_axis + (i * horizontal_direction)] == 0:
                continue
            else: return False
        if Piece.chess_board[vertical_destination][horizontal_destination] == 0:
            return True
        elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
            opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
            capture_piece(opponent_set=opponent_pieces, killed_piece= Piece.chess_board[vertical_destination][horizontal_destination])
            return True
        else:
            return False


    # improve this to one path!
    def valid_move_vert_and_horz(self, vertical_destination: int, horizontal_destination: int) -> bool:
        amount_moved_vertically = vertical_destination - self.vertical_axis
        amount_moved_horizontally = horizontal_destination - self.horizontal_axis
        # if the piece has not moved
        if amount_moved_vertically == 0 and amount_moved_horizontally == 0:
            return False
        # if the piece has moved in both a vertical and horizontal direction
        elif amount_moved_vertically != 0 and amount_moved_horizontally != 0:
            return False
        # then the piece moves in the horizontal direction (vertical destination = current vertical)
        if amount_moved_vertically == 0:
            # finds the direction of movement for the piece
            horizontal_direction = amount_moved_horizontally // abs(amount_moved_horizontally)
            # checks iof the coast is clear
            for i in range(1, abs(amount_moved_horizontally)):
                if Piece.chess_board[self.vertical_axis][self.horizontal_axis + (i * horizontal_direction)] == 0:
                    continue
                else:
                    return False
            if Piece.chess_board[self.vertical_axis][horizontal_destination] == 0:
                return True
            elif Piece.chess_board[self.vertical_axis][horizontal_destination].color != self.color:
                # this will make the opponent_pieces variable black, if color is true (we are white), else opponent_pieces will be white (we are black)
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set = opponent_pieces, killed_piece = Piece.chess_board[vertical_destination][horizontal_destination])
                return True
            else:
                return False
        # then the piece moves in the vertical direction (horizontal destination = current horizontal)
        elif amount_moved_horizontally == 0:
            vertical_direction = amount_moved_vertically // abs(amount_moved_vertically)
            # checks iof the coast is clear
            for i in range(1, abs(amount_moved_vertically)):
                if Piece.chess_board[self.vertical_axis + (i * vertical_direction)][self.horizontal_axis] == 0:
                    continue
                else:
                    return False
            if Piece.chess_board[vertical_destination][self.horizontal_axis] == 0:
                return True
            elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
                # remove peace from other player's list
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set = opponent_pieces, killed_piece = Piece.chess_board[vertical_destination][horizontal_destination])
                return True
            else:
                return False
        # if we get here we had a problem!
        else: return False

    def valid_knight_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        # how much movement the piece has in each direction
        vertical_movement = vertical_destination - self.vertical_axis
        horizontal_movement = horizontal_destination - self.horizontal_axis

        # if we are trying to put the piece outside the board
        if not(0 <= vertical_destination < 8) and not(0 <= horizontal_destination < 8):
            return False

        # if either direction is zero the L shape movement is not satisfied
        elif vertical_movement == 0 or horizontal_movement == 0:
            return False

        # the L shape is satisfied
        elif (abs(vertical_movement) == 2 and abs(horizontal_movement) == 1) or (abs(vertical_movement) == 1 and abs(horizontal_movement) == 2):
            # the position is empty, and we can place the piece there with no extra action!
            if Piece.chess_board[vertical_destination][horizontal_destination] == 0:
                return True
            # we must capture the piece from the other team before being able to place
            elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set=opponent_pieces, killed_piece=Piece.chess_board[vertical_destination][horizontal_destination])
                return True
            # the piece in the position is the same color as the piece we are currently trying to move
            else: return False # Piece.chess_board[vertical_destination][horizontal_destination].color == self.color

        # if we get here then there was an input error
        return False

    def valid_move_pawn(self, vertical_direction: int, horizontal_direction: int) -> bool:

        valid_direction = -1 if self.color else 1
        # trying to move outside the board!
        if not (0 <= self.vertical_axis + vertical_direction  < 8) and (0 <= self.horizontal_axis + horizontal_direction < 8):
            return False

        #normal forward movement (1 direction forward)!
        if ((vertical_direction == valid_direction and horizontal_direction == 0)
                and (Piece.chess_board[self.vertical_axis + vertical_direction][self.horizontal_axis + horizontal_direction] == 0)):
                return True
        # first movement (can move two forward)!
        elif (vertical_direction == (2*valid_direction) and horizontal_direction == 0 and self.first_move
              and (Piece.chess_board[self.vertical_axis + vertical_direction][self.horizontal_axis] == 0)
              and (Piece.chess_board[self.vertical_axis + (vertical_direction//2)][self.horizontal_axis] == 0)):
            return True
        # if we are trying to capture!
        elif vertical_direction == valid_direction and abs(horizontal_direction) == 1:
            # there is no piece to take, or the piece is on the same team!
            if ((Piece.chess_board[self.vertical_axis + vertical_direction][self.horizontal_axis + horizontal_direction] == 0)
                    or
                    Piece.chess_board[self.vertical_axis + vertical_direction][self.horizontal_axis + horizontal_direction].color == self.color):
                return False
            else:
                opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
                capture_piece(opponent_set=opponent_pieces,
                              killed_piece=Piece.chess_board[self.vertical_axis + vertical_direction][self.horizontal_axis + self.horizontal_axis])
                return True
        else: return False
