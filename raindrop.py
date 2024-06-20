import pygame
from pygame.sprite import Sprite


class RainDrops(Sprite):
    """Создает объект дождевой капли"""

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.drop_color
    # создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.drop_width, self.settings.drop_height)
        # self.rect.center = ai_game.screen.rect.center

        self.y = float(self.rect.y)

    def update(self):
        """Перемещает каплю дождя по экрану вниз."""
        # обновление позиции снаряда в вещественном формате
        self.y += self.settings.drop_speed
        self.rect.y = self.y

    def draw_rain_drop(self):
        """Отображение дождевой капли на экране"""

        pygame.draw.rect(self.screen, self.color, self.rect)
