import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Создает объект снаряда в текущей позиции корабля"""

    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.settings = ai_settings
        self.color = self.settings.bullet_color
    # создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop =