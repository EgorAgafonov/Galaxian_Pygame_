import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien's main battle-ship model"""

    def __init__(self, ai_game):
        """Initialize user's main battle-ship and sets starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien_ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True если пришелец находится у края экрана"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельца по экрану влево или вправо."""

        # обновление позиции пришельца в вещественном формате
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x




