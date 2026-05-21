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
        """
        This function checks if the movement requested is actually possible with a queen
        :param vertical_destination: the desired vertical destination
        :param horizontal_destination: the desired horizontal destination
        :return: if the move is actually possible by this queen
        """
        amount_moved_vertical = abs(vertical_destination - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination - self.horizontal_axis)

        # if the piece is actually moving diagonally
        if amount_moved_vertical == amount_moved_horizontal:
            valid_move = Piece.valid_move_diagonal(self, vertical_destination=vertical_destination,
                                                   horizontal_destination=horizontal_destination)
            return valid_move

        #if the queen is moving like a rook
        elif (amount_moved_vertical == 0) or (amount_moved_horizontal == 0):
            valid_move = Piece.valid_move_vert_and_horz(self, vertical_destination=vertical_destination,
                                                        horizontal_destination=horizontal_destination)
            return valid_move
        # if we reach here the move is not good (moved illegally)
        return False


    def move(self, vertical_destination: int, horizontal_destination: int) -> bool :
        """
        This function is used to move the queen piece
        :param vertical_destination: the vertical destination
        :param horizontal_destination: the horizontal destination
        :return: if we can flip the turn to opponent
        """
        check_move = self.valid_move(vertical_destination,
                                     horizontal_destination)
        if check_move:
            good_move = self.place_piece(vertical_desired=vertical_destination,
                             horizontal_desired=horizontal_destination)
            return good_move

        return check_move



