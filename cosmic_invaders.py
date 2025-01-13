import sys

import pygame


class CosmicInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intitialize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Cosmic Invaders")

        # Set background color
        self.bg_color = (0, 20, 50)

    def run_game(self):
        """Start main game loop."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ci = CosmicInvaders()
    ci.run_game()
