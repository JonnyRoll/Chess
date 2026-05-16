from piece import Piece


class King(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=0)

    def move(self, vertical_destination_int: int, horizontal_destination: int) -> bool:
        is_valid_move = self.valid_move_king(vertical_destination_int, horizontal_destination)
        if is_valid_move:
            self.place_piece(vertical_destination_int, horizontal_destination)
        return is_valid_move

    def valid_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        pass

    def in_check(self, vertical_destination, horizontal_destination) -> bool:
        # deciding which sett is the enemy set!

        opponents_set = Piece.black_player_pieces if self.color else Piece.white_player_pieces
        for piece in opponents_set:

            # checks if the specific piece in the opponents set can reach the kings position, if so then the method will return true, indicating the king is in check
            if piece.valid_move(vertical_destination, horizontal_destination):

                return True


        #this indicates the king is not in check!
        return False


    def valid_move_king(self, vertical_destination: int, horizontal_destination: int) -> bool:
        amount_moved_vertical = abs(vertical_destination - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination - self.horizontal_axis)

        # nothing was moved
        if amount_moved_vertical == 0 and amount_moved_horizontal == 0:
            return False
        # the amount moved vertical and horizontal is not valid
        if amount_moved_vertical not in (0, 1) or amount_moved_horizontal not in (0, 1):
            return False

        # we used De_morgana law here
        elif not (0 <= vertical_destination < 8) or not (0 <= horizontal_destination < 8):
           # piece wants to move outside the chess board
            return False

        elif Piece.chess_board[vertical_destination][horizontal_destination] == 0 or Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
            if self.in_check(vertical_destination, horizontal_destination):
                return False
            else:
                return True

        return False










