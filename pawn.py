from piece import Piece

class Pawn(Piece):
    first_move = True
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value,color=color)


    # this is the move method!
    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool:
        # checking if the move is valid
        valid_move = self.valid_move_pawn(vertical_destination_int, horizontal_destination_letter)
        if valid_move:
            self.first_move = False
            #placing the piece is the right position!
            self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)

        return valid_move