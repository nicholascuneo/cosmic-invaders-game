import sys

import pygame

from bullet import Bullet
from enemy import Enemy
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
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start main game loop."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key press down events"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Quit game
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # Fire bullets
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key release up events"""
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old ones"""
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have moved off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create fleet of enemy ships"""
        # Create an enemy ship and find the number of enemies in a row
        # Spacing between each enemy ship is equal to one enemy ship width
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemys_x = available_space_x // (2 * enemy_width)

        # Create row of enemy ships
        for enemy_number in range(number_enemys_x):
            # Create enemy ship and place it in the row
            enemy = Enemy(self)
            enemy.x = enemy_width + 2 * enemy_width * enemy_number
            enemy.rect.x = enemy.x
            self.enemys.add(enemy)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemys.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    rs = RebelStrike()
    rs.run_game()
