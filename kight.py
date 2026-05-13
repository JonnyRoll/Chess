from piece import Piece

class Knight(Piece):
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value)

    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool:
        good_move = self.valid_knight_move(vertical_destination_int, horizontal_destination_letter)
        if good_move:
            self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)

        return good_move