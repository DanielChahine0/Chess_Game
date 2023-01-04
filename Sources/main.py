# This is our main class

# importing modules
import pygame
import sys

# Importing our files
# Constants file
from const import *
from game import Game


class Main:
    # This init method will always be called first
    def __init__(self):
        # Initializing pygame

        pygame.init()
        # Creating a pygame screen and saving it on the variable screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Setting up the captions of the app
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        # Variables set without self for easier use
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board

        # Setting up a pygame file
        while True:
            # Show methods
            game.show_bg(screen)
            game.show_pieces(screen)
            game.show_moves(screen)

            # If we are dragging a piece then show it
            if dragger.dragging:
                # Show the dragged piece on top of the board
                dragger.update_blit(screen)

            # loop through all the events in pygame
            for event in pygame.event.get():

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Save the position
                    dragger.update_mouse(event.pos)

                    # Check if position have a piece
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # If the clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        # Easier use - use the variable piece instead of the whole thing
                        piece = board.squares[clicked_row][clicked_col].piece
                        # Calculate the moves according to the clicked piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        # Save the clicked square if there is a piece
                        # If there is an invalid move that happened, then return
                        # --- the piece to its original position
                        dragger.save_initial(event.pos)
                        # Drag the actual piece
                        dragger.drag_piece(piece)

            # --- Drawing methods on the screen ---
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    # If we are dragging a piece
                    # dragger.dragging is a boolean (True or False)
                    if dragger.dragging:
                        # Update the mouse position
                        dragger.update_mouse(event.pos)

            # --- Drawing methods on the screen ---

                        # Show background first and then the piece
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        # Update the piece position
                        dragger.update_blit(screen)

                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Undrag the piece
                    dragger.undrag_piece()

                # If we are calling Quit then close the app
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update the display after every set of events
            # Should be the last line in our while loop since
            # we want to update the screen after everything
            pygame.display.update()


main = Main()
main.mainloop()
