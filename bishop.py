from piece import Piece

# this is how you do inheritance in python
class Bishop(Piece):

    def __init__(self, name:str , vertical_axis: int, horizontal_axis: int):
        """
        This creates the Bishop piece
        :param name: name of piece
        :param vertical_axis: the column which the piece is in
        :param horizontal_axis: the row which the piece is in
        """
        # calling the super constructor
        super().__init__(name = name, vertical_axis= vertical_axis, horizontal_axis = horizontal_axis, value = 3)

    def valid_move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        return Piece.valid_move_diagonal(self, vertical_destination=vertical_destination, horizontal_destination=horizontal_destination)

    def move(self, vertical_destination_int: int, horizontal_destination: int) -> bool:
        # check that the vertical and horizontal destination are on the board
       if (0 <= vertical_destination_int < 8)  and (0 <= horizontal_destination < 8):
           # if the desired destination is attainable
           is_valid_move = self.valid_move(vertical_destination=vertical_destination_int,
                                           horizontal_destination=horizontal_destination)
           if is_valid_move:
               good_move = self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination)
               return good_move
       # if we reach here we know the move isn't valid!
       return is_valid_move




