from piece import Piece
from bishop import Bishop
from rook import Rook

class Queen(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value, color=color)

    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool :
        amount_moved_vertical = abs(vertical_destination_int - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination_letter - self.horizontal_axis)

        # if both axis change the same amount (diagonal movement) , NOTE (0,0) is handled in the check method!
        if amount_moved_vertical == amount_moved_horizontal:
            valid_move = self.valid_move_diagonal(vertical_destination=vertical_destination_int, horizontal_destination= horizontal_destination_letter)
            if valid_move:
                self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)
            return valid_move

        # if we are trying to move like a rook!
        elif (amount_moved_vertical == 0) or (amount_moved_horizontal == 0):
            valid_move = self.valid_move_vert_and_horz(vertical_destination=vertical_destination_int, horizontal_destination= horizontal_destination_letter)
            if valid_move:
                self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)
            return valid_move
        # if we get here there was a mistake in the input!
        return False



