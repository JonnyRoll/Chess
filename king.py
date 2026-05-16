from piece import *
from piece import Piece


class King():
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int):
        # calling the super constructor
        self.name = name
        self.vertical_axis = vertical_axis
        self.horizontal_axis = horizontal_axis
        self.color = True if name[-1] == 'W' else False

    def in_check(self) -> bool:
        # deciding which sett is the enemy set!
        opponents_set = Piece.black_player_pieces if self.color else Piece.white_player_pieces

        for piece in opponents_set:
            if piece.move(vertical_destination_int=self.vertical_axis, horizontal_destination_letter= self.horizontal_axis):
                return True
            else: continue

        return False


    def valid_move_king(self, vertical_destination: int, horizontal_destination: int) -> bool:
        amount_moved_vertical = abs(vertical_destination - self.vertical_axis)
        amount_moved_horizontal = abs(horizontal_destination - self.horizontal_axis)
        if (amount_moved_vertical == 0 or amount_moved_vertical == 1) and (
                amount_moved_horizontal == 0 or amount_moved_horizontal == 1):
            if Piece.chess_board[vertical_destination][horizontal_destination] == 0 or \
                    Piece.chess_board[vertical_destination][horizontal_destination].color != self.color:
                return True

        return False




