# this is the abstract method library!
from abc import ABC, abstractmethod
from asyncio.windows_events import NULL


def capture_piece (opponent_set: set, killed_piece) -> None:
    opponent_set.remove(killed_piece)

# the ABC says that this is a abstract class (cannot make an instance of it!), can only makes instance of its children
class Piece(ABC):
    chess_board = [[0] * 8 for i in range(8)]
    black_player_pieces = set()
    white_player_pieces = set()
    def __init__(self, name:str ,vertical_axis:int, horizontal_axis:int, value:int):
        self.name = name
        self.vertical_axis = vertical_axis
        self.horizontal_axis = horizontal_axis
        self.value = value
        self.color = True if name[-1] == 'W' else False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    # this is the abstract method!
    @abstractmethod
    def move(self, vertical_destination_int: int, horizontal_destination: int):
        pass

    @abstractmethod
    def valid_move(self, vertical_destination: int, horizontal_destination : int) -> bool:
        pass




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
            return True
        else:
            return False


    # improve this to one path! # dont need this method!
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
                return True
            else:
                return False
        # if we get here we had a problem!
        else: return False


    def place_piece(self, vertical_desired: int, horizontal_desired: int) -> bool:
        # removing the piece from old index
        Piece.chess_board[self.vertical_axis][self.horizontal_axis] = 0
        # storing old indexes
        old_vertical = self.vertical_axis
        old_horizontal = self.horizontal_axis
        opponent_pieces = Piece.black_player_pieces if self.color else Piece.white_player_pieces
        # in the case that we are captaining a piece when moving
        captured_a_piece = False
        temp = 0
        if Piece.chess_board[vertical_desired][horizontal_desired] != 0 and Piece.chess_board[vertical_desired][horizontal_desired].color != self.color:
            # store the opponent piece we are capturing in a temporary box!
            captured_a_piece = True
            temp = Piece.chess_board[vertical_desired][horizontal_desired]
            capture_piece(opponent_set=opponent_pieces,killed_piece=Piece.chess_board[vertical_desired][horizontal_desired])

        # placing our piece down
        Piece.chess_board[vertical_desired][horizontal_desired] = self
        # updating the position values
        self.vertical_axis = vertical_desired
        self.horizontal_axis = horizontal_desired

        # must verier back to the old game state
        if self.king_in_check():
            print('not a valid move king is still in check!')
            #place the piece back to original position!
            Piece.chess_board[old_vertical][old_horizontal] = self
            self.vertical_axis = old_vertical
            self.horizontal_axis = old_horizontal

            if captured_a_piece:
                # adding the piece removed (captured back into the set)
                opponent_pieces.add(temp)
                # even though there are warnings this should always work!
                Piece.chess_board[temp.vertical_axis][temp.horizontal_axis] = temp

            # if no piece was captured!
            else:
                Piece.chess_board[vertical_desired][horizontal_desired] = 0
            return False

        return True


    def current_king(self) -> Piece:
        # finding the position of the current king
        current_set = Piece.white_player_pieces if self.color else Piece.black_player_pieces
        current_king = 'KING_W' if self.color else 'KING_B'
        # this can be any item since it will be replaced with the king element
        for piece in current_set:
            if piece.name == current_king:
                return piece

            # if we get here there is a major problem!
        print(f'{current_king} could not be found')
        return None

    def king_in_check(self) -> bool:
        # deciding which sett is the enemy set!
        opponents_set = Piece.black_player_pieces if self.color else Piece.white_player_pieces
        king = self.current_king()
        for piece in opponents_set:
            # checks if the specific piece in the opponents set can reach the kings position, if so then the method will return true, indicating the king is in check
            if piece.valid_move(king.vertical_axis, king.horizontal_axis):
                return True

        #this indicates the king is not in check!
        return False














# # this might not be needed at all lol
#     def valid_knight_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
#         # how much movement the piece has in each direction
#         vertical_movement = vertical_destination - self.vertical_axis
#         horizontal_movement = horizontal_destination - self.horizontal_axis
#
#         # if we are trying to put the piece outside the board
#         if not(0 <= vertical_destination < 8) and not(0 <= horizontal_destination < 8):
#             return False
#
#         # if either direction is zero the L shape movement is not satisfied
#         elif vertical_movement == 0 or horizontal_movement == 0:
#             return False
#
#         # the L shape is satisfied
#         elif (abs(vertical_movement) == 2 and abs(horizontal_movement) == 1) or (abs(vertical_movement) == 1 and abs(horizontal_movement) == 2):
#             # the position is empty, and we can place the piece there with no extra action!
#             if Piece.chess_board[vertical_destination][horizontal_destination] == 0:
#                 return True
#             # we must capture the piece from the other team before being able to place
#             elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
#                 return True
#             # the piece in the position is the same color as the piece we are currently trying to move
#             else: return False # Piece.chess_board[vertical_destination][horizontal_destination].color == self.color
#
#         # if we get here then there was an input error
#         return False
# # this might not be needed
#     def valid_move_pawn(self, vertical_destination: int, horizontal_destination: int) -> bool:
#         #finding how much the total movement is
#         vertical_movement = vertical_destination - self.vertical_axis
#         horizontal_movement = horizontal_destination - self.horizontal_axis
#
#         #deciding which direction the piece can move based on color
#         # NOTE if self.color is true we are on white team
#         valid_direction = -1 if self.color else 1
#
#         # if the pawn moves in its traditional manner (moves one square vertically)
#         if vertical_movement == valid_direction and horizontal_movement == 0:
#             return Piece.chess_board[vertical_destination][horizontal_destination] == 0
#
#         # in the case it's the pawn first move it can jump two pieces forward NOTE the two square need to be empty!
#         elif vertical_movement == (2*valid_direction) and horizontal_movement == 0 and self.first_move:
#             #checking if both square are free!
#             return (Piece.chess_board[vertical_destination][horizontal_destination] == 0
#                     and Piece.chess_board[self.vertical_axis + valid_direction][horizontal_destination] == 0)
#
#         #this is when a pawn wants to capture its diagonal counterpart
#         elif vertical_movement == valid_direction and abs(horizontal_movement) == 1:
#             # if the diagonal square is not occupied by an enemy piece
#             if (Piece.chess_board[vertical_destination][horizontal_destination] == 0
#                 or Piece.chess_board[vertical_destination][horizontal_destination].color == self.color):
#
#                 return False
#             # the diagonal piece is occupied by an enemy piece
#             else:
#                 return True
#         # if we get here the move is not valid!
#         return False
#
#





