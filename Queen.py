from piece import Piece
from bishop import Bishop
from rook import Rook

class Queen(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value, color=color)

    def move(self, move_vertical: int, move_horizontal: int) -> bool :
        if (move_vertical == 0) and (move_horizontal == 0):
            return False
        if (0 <= move_vertical + self.vertical_axis < 7) and (0 <= move_horizontal + self.horizontal_axis < 7):
            if move_vertical == move_horizontal:
                good_move = self.valid_move_diagonal(vertical_direction=move_vertical, horizontal_direction=move_horizontal)
                if good_move:
                    amount_move = abs(move_vertical)
                    x_index = self.vertical_axis + (abs(amount_move) * (move_vertical // abs(move_vertical)))
                    y_index = self.horizontal_axis + (
                                abs(amount_move) * (move_horizontal // abs(move_horizontal)))
                    self.place_piece(vertical_desired=x_index, horizontal_desired=y_index)
                    return True
            # we are saying the move is horizontal! ( like a rook )
            elif move_vertical == 0:
                good_move = self.valid_move_vert_and_horz(amount=move_horizontal, move_horizontally=True)
                if good_move:
                    self.place_piece(vertical_desired=self.vertical_axis,horizontal_desired=self.horizontal_axis + move_horizontal)
                    return True
            elif move_horizontal == 0:
                good_move = self.valid_move_vert_and_horz(amount = move_vertical, move_horizontally=False)
                if good_move:
                    self.place_piece(vertical_desired=self.vertical_axis + move_vertical,horizontal_desired=self.horizontal_axis)
                    return True
        # if you get here none of the valid moves are possible!
        return False



