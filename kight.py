from piece import Piece

class Knight(Piece):
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int):
        """
        This creates the knight piece
        :param name: name of piece
        :param vertical_axis: the column which the piece is in
        :param horizontal_axis: the row which the piece is in
        """
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=3)

    def valid_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        This function checks if the movement requested towards the knight is valid,
        unlike other pieces the knight can jump over pieces, thus we must only check if the amount requested to move is a valid amount and if the square it wants to move to is available for it to move to
        :param vertical_destination: the destination column of the knight
        :param horizontal_destination: the destination row of the knight
        :return: if the knight can move to that position
        """
        # how much movement the piece has in each direction
        vertical_movement = vertical_destination - self.vertical_axis
        horizontal_movement = horizontal_destination - self.horizontal_axis

        # if we are trying to put the piece outside the board
        if not (0 <= vertical_destination < 8) and not (0 <= horizontal_destination < 8):
            return False

        # if either direction is zero the L shape movement is not satisfied
        elif vertical_movement == 0 or horizontal_movement == 0:
            return False

        # the L shape is satisfied
        elif (abs(vertical_movement) == 2 and abs(horizontal_movement) == 1) or (
                abs(vertical_movement) == 1 and abs(horizontal_movement) == 2):
            # the position is empty, and we can place the piece there with no extra action!
            if Piece.chess_board[vertical_destination][horizontal_destination] == 0:
                return True
            # we must capture the piece from the other team before being able to place
            elif Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
                return True
            # the piece in the position is the same color as the piece we are currently trying to move
            else:
                return False  # Piece.chess_board[vertical_destination][horizontal_destination].color == self.color

        # if we get here then there was an input error
        return False

    def move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        """
        This function is used to move the knight piece
        :param vertical_destination: the vertical destination
        :param horizontal_destination: the horizontal destination
        :return: if we can flip to opponent's turn
        """
        valid_move = self.valid_move(vertical_destination, horizontal_destination)
        if valid_move:
            good_move = self.place_piece(vertical_desired=vertical_destination, horizontal_desired=horizontal_destination)
            return good_move

        return valid_move