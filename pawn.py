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
        current_set = Piece.white_player_pieces if self.color else Piece.black_player_pieces
        while True:
            promote = input('queen, bishop, rook, knight: ')
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



    def valid_move(self, vertical_destination: int, horizontal_destination : int) -> bool:
        # finding how much the total movement is
        vertical_movement = vertical_destination - self.vertical_axis
        horizontal_movement = horizontal_destination - self.horizontal_axis

        # deciding which direction the piece can move based on color
        # NOTE if self.color is true we are on white team
        valid_direction = -1 if self.color else 1

        # if the pawn moves in its traditional manner (moves one square vertically)
        if vertical_movement == valid_direction and horizontal_movement == 0:
            return Piece.chess_board[vertical_destination][horizontal_destination] == 0

        # in the case it's the pawn first move it can jump two pieces forward NOTE the two square need to be empty!
        elif vertical_movement == (2 * valid_direction) and horizontal_movement == 0 and self.first_move:
            # checking if both square are free!
            return (Piece.chess_board[vertical_destination][horizontal_destination] == 0
                    and Piece.chess_board[self.vertical_axis + valid_direction][horizontal_destination] == 0)

        # this is when a pawn wants to capture its diagonal counterpart
        elif vertical_movement == valid_direction and abs(horizontal_movement) == 1:
            # if the diagonal square is not occupied by an enemy piece
            if (Piece.chess_board[vertical_destination][horizontal_destination] == 0
                    or Piece.chess_board[vertical_destination][horizontal_destination].color == self.color):

                return False
            # the diagonal piece is occupied by an enemy piece
            else:
                return True
        # if we get here the move is not valid!
        return False

    # this is the move method!
    def move(self, vertical_destination: int, horizontal_destination: int) -> bool:
        # checking if the move is valid
        valid_move = self.valid_move(vertical_destination, horizontal_destination)

        if valid_move:
            self.first_move = False
            # placing the piece is the right position!
            self.place_piece(vertical_desired=vertical_destination, horizontal_desired=horizontal_destination)

            # if he pawns has reached the end of the board (promotion!)
            reached_end = 0 if self.color else 7
            if vertical_destination == reached_end:
                self.promote()

        return valid_move