from piece import Piece

class Rook(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int):
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value)

    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool:
        is_valid_move = self.valid_move_vert_and_horz(vertical_destination= vertical_destination_int, horizontal_destination= horizontal_destination_letter)
        if is_valid_move:
            self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)
        return is_valid_move


