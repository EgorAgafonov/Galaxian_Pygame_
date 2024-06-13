import pygame


class Ship():
    """User's main battle-ship model"""

    def __init__(self, ai_settings, screen):
        """Initialize user's main battle-ship and sets starting position."""

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/user_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False

    def update(self):
        """Refreshes user's ship position according the flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Displays the ship at its current position."""

        self.screen.blit(self.image, self.rect)
