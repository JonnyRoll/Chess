from piece import Piece

# this is how you do inheritance in python
class Bishop(Piece):
    def __init__(self, name:str , vertical_axis: int, horizontal_axis: int, value: int):
        # calling the super constructor
        super().__init__(name = name, vertical_axis= vertical_axis, horizontal_axis = horizontal_axis, value = value)


    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool:
        # check that the vertical and horizontal destination are on the board
       if (0 <= vertical_destination_int < 8)  and (0 <= horizontal_destination_letter < 8):
           # if the desired destination is attainable
           is_valid_move = self.valid_move_diagonal(vertical_destination=vertical_destination_int,
                                                     horizontal_destination=horizontal_destination_letter)
           if is_valid_move:
               self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)
            # returns weather the move is valid!
           return is_valid_move
       # if we reach here we know the move isn't valid!
       return False




