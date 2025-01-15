import sys

import pygame

from settings import Settings
from ship import Ship


class RebelStrike:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intitialize the game and create game resources."""
        pygame.init()
        # Call and create instance of Settings class
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rebel Strike")

        self.ship = Ship(self)

    def run_game(self):
        """Start main game loop."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    rs = RebelStrike()
    rs.run_game()
