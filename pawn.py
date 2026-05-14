from os import remove

from piece import Piece, capture_piece

class Pawn(Piece):
    first_move = True
    def __init__(self, name: str, vertical_axis: int, horizontal_axis: int, value: int):
        # calling the super constructor
        super().__init__(name=name, vertical_axis=vertical_axis, horizontal_axis=horizontal_axis, value=value)

    next_queens_W = 2
    next_queens_B = 2
    next_bishop_W = 3
    next_bishop_B = 3
    next_knight_W = 3
    next_knight_B = 3
    next_rook_W = 3
    next_rook_B = 3
    def promote(self):
        # importing here prevents the circular loop error
        from game import create_pieces, place_pieces_on_board
        print('which piece would you like to promote to?')
        promote = input('queen, bishop, rook, knight')
        current_set = Piece.white_player_pieces if self.color else Piece.black_player_pieces
        while True:
            match promote:
                case 'queen':
                    from Queen import Queen
                    piece_name = f'Q{Pawn.next_queens_W}_W' if self.color else f'Q{Pawn.next_queens_B}_B'
                    if self.color: Pawn.next_queens_W += 1
                    else: Pawn.next_queens_B += 1
                    new_piece = Queen(name=piece_name, vertical_axis=self.vertical_axis, horizontal_axis=self.horizontal_axis, value=9)
                    create_pieces(new_piece)
                    place_pieces_on_board(new_piece)
                    capture_piece(opponent_set=current_set, killed_piece=self)
                    break
                case 'bishop':
                    from bishop import Bishop
                    piece_name = f'b{Pawn.next_bishop_W}_W' if self.color else f'b{Pawn.next_bishop_B}_B'
                    if self.color: Pawn.next_bishop_W += 1
                    else: Pawn.next_bishop_B += 1
                    new_piece = Bishop(name=piece_name,vertical_axis=self.vertical_axis, horizontal_axis=self.horizontal_axis, value=3)
                    create_pieces(new_piece)
                    place_pieces_on_board(new_piece)
                    capture_piece(opponent_set=current_set, killed_piece=self)
                    break
                case 'rook':
                    from rook import Rook
                    piece_name = f'b{Pawn.next_rook_W}_W' if self.color else f'b{Pawn.next_rook_B}_B'
                    if self.color:
                        Pawn.next_rook_W += 1
                    else:
                        Pawn.next_rook_B += 1
                    new_piece = Rook(name= piece_name, vertical_axis=self.vertical_axis, horizontal_axis=self.horizontal_axis, value=5)
                    create_pieces(new_piece)
                    place_pieces_on_board(new_piece)
                    capture_piece(opponent_set=current_set, killed_piece=self)
                    break
                case 'knight':
                    from kight import Knight
                    piece_name = f'b{Pawn.next_knight_W}_W' if self.color else f'b{Pawn.next_knight_B}_B'
                    new_piece = Knight(name=piece_name, vertical_axis=self.vertical_axis, horizontal_axis=self.horizontal_axis, value=3)
                    create_pieces(new_piece)
                    place_pieces_on_board(new_piece)
                    capture_piece(opponent_set=current_set, killed_piece=self)
                    break
                # all other cases
                case _ :
                    print('invalid input please try again!')




    # this is the move method!
    def move(self, vertical_destination_int: int, horizontal_destination_letter: int) -> bool:
        # checking if the move is valid
        valid_move = self.valid_move_pawn(vertical_destination_int, horizontal_destination_letter)
        if valid_move:
            self.first_move = False
            #placing the piece is the right position!
            self.place_piece(vertical_desired=vertical_destination_int, horizontal_desired=horizontal_destination_letter)
            # if the white piece reached the end
            if self.color == True and self.vertical_axis == 0:
                self.promote()
            # if the black piece reached the end
            elif self.color == False and self.vertical_axis == 7:
                self.promote()

        return valid_move