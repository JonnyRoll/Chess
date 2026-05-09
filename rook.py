from piece import Piece

class Rook(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value, color=color)

    def move_horizontally(self, amount: int) -> bool:
        # this will check if the input is NOT valid!
        if not (0 <= self.horizontal_axis + amount < 8):
            return False

        # in the case that the amount is valid we will check if the path is clear
        valid_move = self.valid_move_vert_and_horz(amount=amount, move_horizontally=True)
        if valid_move:
            self.place_piece(vertical_desired=self.vertical_axis, horizontal_desired=self.horizontal_axis + amount)
            return True

        return False




    def move_vertically(self, amount: int) -> bool:
        # this will check if the input is NOT valid!
        if not (0 <= self.vertical_axis + amount < 8):
            return False

        # in the case that the amount is valid we will check if the path is clear
        valid_move = self.valid_move_vert_and_horz(amount=amount, move_horizontally=False)
        if valid_move: # if the path is clear we will place the piece in the right position and update
            self.place_piece(vertical_desired=self.vertical_axis + amount, horizontal_desired=self.horizontal_axis)
            return True

        return False
