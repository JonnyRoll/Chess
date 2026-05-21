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
        """ This is the constructor for the piece object, it assigns the values to all the variables"""
        self.name = name
        self.vertical_axis = vertical_axis
        self.horizontal_axis = horizontal_axis
        self.value = value
        self.color = True if name[-1] == 'W' else False

    def __str__(self):
        """This function returns the string representation of the piece object"""
        return self.name

    def __repr__(self):
        """This function returns the string representation of the piece object while printing in a loop"""
        return self.name

    # this is the abstract method!
    @abstractmethod
    def move(self, vertical_destination_int: int, horizontal_destination: int):
        pass

    @abstractmethod
    def valid_move(self, vertical_destination: int, horizontal_destination : int) -> bool:
        pass




    def valid_move_diagonal(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        This function validates a diagonal movement, it does so by checking if the amount you want to move vertical = the amount moved horizontally
        afterward it checks if all the blocks the piece must move passed in empty.
        If the move is valid then the definition will return True
        If the move is not valid then it will return False
        """
        amount_moved_vertical = vertical_destination - self.vertical_axis
        amount_moved_horizontal = horizontal_destination - self.horizontal_axis
        # if we do not move from at least 1 axis
        if amount_moved_vertical== 0 or amount_moved_horizontal == 0:
            return False
        # if both axis don't move the same amount
        elif abs(amount_moved_vertical) != abs(amount_moved_horizontal):
            return False

        # will determine if we are moving up higher on the board (negative) for vertical and move left on the board (negative)
        vertical_direction = amount_moved_vertical // abs(amount_moved_vertical)
        horizontal_direction = amount_moved_horizontal // abs(amount_moved_horizontal)
        #checks all the pieces the piece has to pass over
        for i in range(1, abs(amount_moved_vertical)):
            if Piece.chess_board[self.vertical_axis + (i * vertical_direction)][self.horizontal_axis + (i * horizontal_direction)] == 0:
                continue
            else: return False # there is a piece in the way

        if Piece.chess_board[vertical_destination][horizontal_destination] == 0:
            return True
        elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color: # if we have to capture an opponent's piece
            return True
        else: # There is one of their pieces on the board
            return False



    def valid_move_vert_and_horz(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        This method checks if the 'straight' lined movement is valid,
        first we decide if we are going to check if the piece is moving vertically or horizontally.
        if the piece is moving vertically we will move along the vertical axis to check if all squares inbetween the original and desired square is empty (allowing for a valid move)
        if the piece is found to move horizontally the same action will be done as the vertical check (but just incrementing the horizontal direction instead)
        """
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
            # checks every intermediate square and varifies it is empty
            for i in range(1, abs(amount_moved_horizontally)):
                if Piece.chess_board[self.vertical_axis][self.horizontal_axis + (i * horizontal_direction)] == 0:
                    continue
                else: # if the square has a piece on it
                    return False
            # makes sure the desired square deos not have a piece of the same team on it.
            if Piece.chess_board[self.vertical_axis][horizontal_destination] == 0:
                return True
            elif Piece.chess_board[self.vertical_axis][horizontal_destination].color != self.color:
                return True
            else:
                return False

        # then the piece moves in the vertical direction (horizontal destination = current horizontal)
        elif amount_moved_horizontally == 0:
            vertical_direction = amount_moved_vertically // abs(amount_moved_vertically)
            # checks every intermediate square and varifies it is empty
            for i in range(1, abs(amount_moved_vertically)):
                if Piece.chess_board[self.vertical_axis + (i * vertical_direction)][self.horizontal_axis] == 0:
                    continue
                else: # if the square (we are currently checking) has a piece on it
                    return False
            # makes sure the desired square deos not have a piece of the same team on it.
            if Piece.chess_board[vertical_destination][self.horizontal_axis] == 0:
                return True
            elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
                return True
            else:
                return False

        # if we get here we had a problem! basically not possible
        else:
            print('you should not have reached here')
            return False


    def place_piece(self, vertical_desired: int, horizontal_desired: int) -> bool:
        """
        This function defines how a piece will be moved from its current position on the board to ints new position on the board
        additionally the function stores the old position of the piece, in the case the next move is not valid (still is in check), this allows us to revert back to the old game state if needed.
        Additionally, in the case that we must capture a piece on this move. A flag will go up indicating we have killed a piece in this action, then the newly killed piece will be placed in a temporary holder.
        if the move is valid the captured piece will be discarded, if the move is invalid however we will place the piece back in the correct sett before going back to the old game state.
        """
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
        """
        This function will check the correct set and find the king piece of said set
        """
        # finding the position of the current king
        current_set = Piece.white_player_pieces if self.color else Piece.black_player_pieces
        current_king = 'KING_W' if self.color else 'KING_B'
        # this can be any item since it will be replaced with the king element
        for piece in current_set:
            if piece.name == current_king:
                return piece

        # if we get here there is a major problem! (means the king does not exist)
        print(f'{current_king} could not be found')
        return None

    def king_in_check(self) -> bool:
        """
        This function will check the correct set and determine if any piece from the enemy set can reach the kings position
        if so the king is in check.

        :return: if the king of the set is in check (if returned true then the king is in check)
        """
        opponents_set = Piece.black_player_pieces if self.color else Piece.white_player_pieces
        king = self.current_king()
        for piece in opponents_set:
            # checks if the specific piece in the opponents set can reach the kings position, if so then the method will return true, indicating the king is in check
            if piece.valid_move(king.vertical_axis, king.horizontal_axis):
                return True

        #this indicates the king is not in check!
        return False
