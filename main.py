import pygame
import sys
from engine.game import Game

def main():
    """Entry point for the business simulation game."""
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()