from piece import Piece

class Queen(Piece):

    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int):
        """
        This creates the queen  piece
        :param name: name of piece
        :param vertical_axis: the column which the piece is in
        :param horizontal_axis: the row which the piece is in
        """
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=9)

    def valid_move(self, vertical_destination, horizontal_destination) -> bool:
        from bishop import Bishop
        from rook import Rook
        amount_moved_vertical = abs(vertical_destination - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination - self.horizontal_axis)

        if amount_moved_vertical == amount_moved_horizontal:
            valid_move = Piece.valid_move_diagonal(self, vertical_destination=vertical_destination,
                                                   horizontal_destination=horizontal_destination)
            return valid_move

        elif (amount_moved_vertical == 0) or (amount_moved_horizontal == 0):
            valid_move = Piece.valid_move_vert_and_horz(self, vertical_destination=vertical_destination,
                                                        horizontal_destination=horizontal_destination)
            return valid_move
        # if we reach here the move is not good
        return False


    def move(self, vertical_destination: int, horizontal_destination: int) -> bool :

        check_move = self.valid_move(vertical_destination,
                                     horizontal_destination)
        if check_move:
            good_move = self.place_piece(vertical_desired=vertical_destination,
                             horizontal_desired=horizontal_destination)
            return good_move

        return check_move



