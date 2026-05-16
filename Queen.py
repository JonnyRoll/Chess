from piece import Piece

class Queen(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value)

    def valid_move(self, vertical_destination_int, horizontal_destination_letter) -> bool:
        from bishop import Bishop
        from rook import Rook
        amount_moved_vertical = abs(vertical_destination_int - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination_letter - self.horizontal_axis)

        if amount_moved_vertical == amount_moved_horizontal:
            valid_move = Piece.valid_move_diagonal(self,vertical_destination=vertical_destination_int,
                                                  horizontal_destination=horizontal_destination_letter)
            return valid_move

        elif (amount_moved_vertical == 0) or (amount_moved_horizontal == 0):
            valid_move = Piece.valid_move_vert_and_horz(self, vertical_destination=vertical_destination_int,
                                                       horizontal_destination=horizontal_destination_letter)
            return valid_move
        # if we reach here the move is not good
        return False


    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool :

        check_move = self.valid_move(vertical_destination_int = vertical_destination_int,horizontal_destination_letter= horizontal_destination_letter)
        if check_move:
            self.place_piece(vertical_desired=vertical_destination_int,
                             horizontal_desired=horizontal_destination_letter)
            return check_move

        return False



