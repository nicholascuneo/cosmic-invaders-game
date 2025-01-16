import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, rs_game):
        """Initialize ship and set its starting position"""
        self.screen = rs_game.screen
        self.settings = rs_game.settings
        self.screen_rect = rs_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load("images/xwing.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            # self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # self.rect.x -= 1

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
