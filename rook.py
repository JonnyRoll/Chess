from piece import Piece

class Rook(Piece):



    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int):
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value)

    def valid_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        return Piece.valid_move(self, vertical_destination=vertical_destination, horizontal_destination=horizontal_destination)

    def move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        is_valid_move = self.valid_move(vertical_destination= vertical_destination, horizontal_destination= horizontal_destination)
        if is_valid_move:
            good_move = self.place_piece(vertical_desired=vertical_destination, horizontal_desired=horizontal_destination)
            return good_move
        return is_valid_move


