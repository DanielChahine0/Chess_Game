import pygame

from const import *
from board import Board
from dragger import Dragger


# Game class
# This file is responsible for all the rendering methods


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Blit on the screen methods
    def show_bg(self, surface):
        # Loop all the rows in our board
        for row in range(ROWS):
            # Loop all the columns in our board
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    # Light Green Color
                    color = (234, 235, 200)
                else:
                    # Dark Green Color
                    color = (119, 154, 88)

                # creating the rectangle that will be drawn
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    # Set the texture to 80 pixels
                    piece.set_texture(80)

                    # All pieces except the piece that we are dragging
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        # This will center the image
                        img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, screen):
        # Show the moves when we are dragging a piece
        if self.dragger.dragging:
            piece = self.dragger.piece
            # Looping through all valid moves
            for move in piece.moves:
                # Creating a color
                color = '#e83838' if (move.final.row + move.final.col) % 2 == 0 else '#a31c1c'
                # Rectangle
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)

                # Blitting the rectangle1
                pygame.draw.rect(screen, color, rect)
