from piece import Piece

class Knight(Piece):
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value, color=color)

    def move(self, vertical_direction: int, horizontal_direction: int) -> bool:
        good_move = self.valid_knight_move(vertical_direction, horizontal_direction)
        if good_move:
            self.place_piece(vertical_desired= self.vertical_axis + vertical_direction, horizontal_desired= self.horizontal_axis + horizontal_direction)
        return good_move