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
        self.x = float(self.rect.y)

    def update(self):
        """Перемещение дождевого потока вниз экрана"""

        self.y += self.settings.drop_speed
        self.x += self.settings.drop_wind
        self.rect.y = self.y
        self.rect.x = self.x

    # def draw_drop(self, ai_game):
    #     """Отображение капли на экране"""

    #     self.screen = ai_game
    #     pygame.draw.rect(self.screen, self.color, self.rect)
