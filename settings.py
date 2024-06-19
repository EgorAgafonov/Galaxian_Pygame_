import pygame

"""Класс с настройками игры Alien_Invasion"""


class Settings:
    def __init__(self):
        """Инициализируем настройки игры"""

        self.screen_width = 1920
        self.screen_height = 1097
        self.bg_color = (4, 2, 80)
        self.bckgrnd_screen = pygame.image.load('images/background_screen.png')
        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_limit = 4

