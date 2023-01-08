# Importing all constants
from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        # Creating a list of 8 0s for each column
        self.squares: list[list] = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(COLS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    # Calculate the possible moves
    def calc_moves(self, piece, row, col):
        """
        Calculate all the possible moves on a specific piece
        for all different positions
        """
        def pawn_moves():
            # If the piece has moved before then it is able to move only 1 step
            # If the piece has not moved then it can move 2 steps
            steps = 1 if piece.moved else 2

            # Vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row):
                    # If the square in front of the pawn is empty
                    if self.squares[move_row][col].is_empty():
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new move
                        piece.add_move(move)
                    # If the square in front of the pawn is not empty
                    else:
                        break
                # not in range
                else:
                    break

            # Diagonal moves - When taking a piece
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    # If square has an enemy then we can take it
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # Create an initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new move
                        piece.add_move(move)

        def knight_moves():
            possible_moves = [
                (row-2, col+1),
                (row-2, col-1),
                (row-1, col+2),
                (row-1, col-2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col+2),
                (row+1, col-2),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                # Checks if the possible row AND col is in the board
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        # Create squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new valid move
                        piece.add_move(move)

        def straight_line_moves(incrs):
            pass

        # If the piece is a Pawn
        if isinstance(piece, Pawn):
            pawn_moves()

        # If the piece is a knight
        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straight_line_moves([
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1)
            ])

        elif isinstance(piece, Rook):
            straight_line_moves([
                (-1, 0),  # up
                (0, 1),   # right
                (1, 0),   # down
                (0, -1)   # left

            ])

        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1),
                (-1, 0),  # up
                (0, 1),  # right
                (1, 0),  # down
                (0, -1)  # left
            ])

        elif isinstance(piece, King):
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):

        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other, 1, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 6, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
