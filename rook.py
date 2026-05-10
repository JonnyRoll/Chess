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

    def move(self, vertical_move: int, horizontal_move: int) -> bool:
        if (vertical_move == 0) and (horizontal_move == 0):
            return False

        elif (vertical_move != 0) and (horizontal_move != 0):
            return False

        # no vertical movement
        elif vertical_move == 0:
            return self.move_horizontally(amount=horizontal_move)
        # no horizontal movement
        elif horizontal_move == 0:
            return self.move_vertically(amount=vertical_move)

         #if we get here there was a problem in the movement
        return False
