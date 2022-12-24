import os


class Piece:
    def __init__(self, name, color, value, texture=None, texturerect=None):
        self.name = name
        self.color = color
        # My pieces will have a positive value
        # Opponents pieces will have a negative value
        value_sign = 1 if color == "white" else -1
        self.value = value*value_sign
        # This is an image
        self.texture = texture
        self.moves = []
        self.moved = False
        self.set_texture()
        self.texture_rect = texturerect

    def set_texture(self, size=80):
        self.texture = os.path.join(f"assets/images/imgs-{size}px/{self.color}_{self.name}.png")

    def add_move(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        # The color will determine the direction of the pieces
        self.dir = -1 if color == "white" else 1
        # Super init will be our init for our piece function
        super().__init__("pawn", color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        # Super init will be our init for our piece function
        super().__init__("knight", color, 3.0)


class Bishop(Piece):
    def __init__(self, color):
        # Super init will be our init for our piece function
        # Bishops are a little better than knights
        super().__init__("bishop", color, 3.001)


class Rook(Piece):
    def __init__(self, color):
        # Super init will be our init for our piece function
        super().__init__("rook", color, 5.0)


class Queen(Piece):
    def __init__(self, color):
        # Super init will be our init for our piece function
        super().__init__("queen", color, 9.0)


class King(Piece):
    def __init__(self, color):
        # Super init will be our init for our piece function
        # Tell the computer that this is the most important piece
        super().__init__("king", color, 10000000.0)
