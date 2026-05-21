from piece import Piece

class Rook(Piece):



    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int):
        """
        This creates the rook piece
        :param name: name of piece
        :param vertical_axis: the column which the piece is in
        :param horizontal_axis: the row which the piece is in
        """
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=5)

    def valid_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        Checks if the move is valid using the vertical or horizontal move validator function
        :param vertical_destination: the desired vertical destination
        :param horizontal_destination: the desired horizontal destination
        :return: if the move is valid
        """
        return Piece.valid_move_vert_and_horz(self, vertical_destination=vertical_destination, horizontal_destination=horizontal_destination)

    def move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        calls the move validation check before moving the chess piece, this is the most outer call for rook piece
        :param vertical_destination: the desired vertical destination
        :param horizontal_destination: the desired horizontal destination
        :return:  if we can flip to opponent's turn
        """
        is_valid_move = self.valid_move(vertical_destination= vertical_destination, horizontal_destination= horizontal_destination)
        if is_valid_move:
            good_move = self.place_piece(vertical_desired=vertical_destination, horizontal_desired=horizontal_destination)
            return good_move
        return is_valid_move


