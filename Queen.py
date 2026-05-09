from piece import Piece
from bishop import Bishop
from rook import Rook

class Queen(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value, color=color)

    def valid_move(self, amount:int, moving_diagonal: bool) -> bool :
        if moving_diagonal:
            while True:
                try:
                    x_dir = int(input('are we moving left (negative #) or right (positive #): '))
                    break
                except ValueError:
                    continue

            while True:
                try:
                    y_dir = int(input('are we moving up (negative #) or down (positive #): '))
                    break
                except ValueError:
                    continue

            return self.valid_move_diagonal(amount=amount, vertical_direction=x_dir, horizontal_direction=y_dir)
        else:
            while True:
                try:
                    by_row = int(input('are we moving by row (positive) or column (negative and zero) '))
                    break
                except ValueError:
                    continue

            by_row_bool = by_row > 0
            return self.valid_move_vert_and_horz(amount=amount, move_horizontally=by_row_bool)


