import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Class to represent a single enemy in the fleet"""

    def __init__(self, rs_game):
        """Initialize enemy ship and set its starting position"""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings

        # Load enemy image and set its rect attribute
        self.image = pygame.image.load("images/tiefighter.png")
        self.rect = self.image.get_rect()

        # Start each new enemy ship near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true is enemy reaches screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move enemy right or left"""
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x
