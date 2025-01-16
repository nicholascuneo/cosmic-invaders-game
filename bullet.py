import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets fired from the ship"""

    def __init__(self, rs_game):
        """Create a bullet object at ship's current position"""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) then set to correct position of ship.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = rs_game.ship.rect.midtop

        # Store bullet's position as float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up screen"""
        # Update float position of bullet
        self.y -= self.settings.bullet_speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
