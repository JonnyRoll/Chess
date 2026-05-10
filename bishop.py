from piece import Piece

# this is how you do inheritance in python
class Bishop(Piece):
    def __init__(self, name:str , vertical_axis: int, horizontal_axis: int, value: int, color: bool):
        # calling the super constructor
        super().__init__(name = name, vertical_axis= vertical_axis, horizontal_axis = horizontal_axis, value = value, color = color)


    def move(self, vertical_direction: int, horizontal_direction: int) -> bool:
       if (0 <= vertical_direction + self.vertical_axis < 8) and (0 <= horizontal_direction + self.horizontal_axis < 8):
           check_if_valid = self.valid_move_diagonal(vertical_direction=vertical_direction,
                                                     horizontal_direction=horizontal_direction)
           if check_if_valid:
               amount_move = abs(vertical_direction)
               vertical_index = self.vertical_axis + (abs(amount_move) * (vertical_direction // abs(vertical_direction)))
               horizontal_index = self.horizontal_axis + (abs(amount_move) * (horizontal_direction // abs(horizontal_direction)))
               self.place_piece(vertical_desired=vertical_index, horizontal_desired=horizontal_index)
            # returns weather the move is valid!
           return check_if_valid
       # if we reach here we know the move isn't valid!
       return False




