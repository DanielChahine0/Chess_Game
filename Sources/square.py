class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    # Return the piece if it's not empty
    def has_piece(self):
        return self.piece is not None

    # Returns False if there is a piece
    def is_empty(self):
        return not self.has_piece()

    # Returns True if there is a piece AND if it's the same color
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    # Returns True if there is a piece AND if it's a different color
    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color

    # Returns True if there are no pieces OR if the piece is a different color
    def is_empty_or_rival(self, color):
        return self.is_empty() or self.has_rival_piece(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            # If this is outside the boards
            if arg < 0 or arg > 7:
                return False

        return True
