import pygame
from const import *


class Dragger:

    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None  # The piece that is being dragged
        self.dragging = False

# Blitting section ------------------------------------------------------------
    # Update the image of the chosen piece
    def update_blit(self, surface):
        # texture
        # When we are dragging a piece, update the texture to 128 to make it bigger
        self.piece.set_texture(size=128)

        # Save the path of the texture as texture
        texture = self.piece.texture

        # save the new image of the texture in the variable img
        img = pygame.image.load(texture)

        # Centering the image
        # The center of the image will be the position of the mouse
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        # blitting the image
        surface.blit(img, self.piece.texture_rect)
# ---------------------------------------=-------------------------------------

    # Update the mouse position
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos  # pos is going to be a tuple (x, y)

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        # Save the piece we are dragging
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

