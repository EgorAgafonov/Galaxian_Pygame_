import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien's main battle-ship model"""

    def __init__(self, ai_game):
        """Initialize user's main battle-ship and sets starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
