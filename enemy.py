import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Class to represent a single enemy in the fleet"""

    def __init__(self, rs_game):
        """Initialize enemy ship and set its starting position"""
        super().__init__()
        self.screen = rs_game.screen

        # Load enemy image and set its rect attribute
        self.image = pygame.image.load("images/tiefighter.png")
        self.rect = self.image.get_rect()

        # Start each new enemy ship near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
