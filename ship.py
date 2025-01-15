import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ci_game):
        """Initialize ship and set its starting position"""
        self.screen = ci_game.screen
        self.screen_rect = ci_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load("images/xwing.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
