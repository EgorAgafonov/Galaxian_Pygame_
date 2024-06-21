import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    """Создает объект дождевой капли"""

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.drop_color
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.height
        self.rect.y = 0

        self.y = float(self.rect.y)
