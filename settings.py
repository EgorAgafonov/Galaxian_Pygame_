"""Класс с настройками игры Alien_Invasion"""
import pygame
from random import randint


class Settings:
    def __init__(self):
        """Инициализируем настройки игры"""

        self.background_color = (4, 2, 80)
        self.background_image = pygame.image.load('images/background_screen.png')
        self.screen_width = self.background_image.get_width()
        self.screen_height = self.background_image.get_height()

        self.meteor_speed = 3
        self.ship_speed = 1.5
        self.alien_speed = 1

        self.fleet_drop_speed = 20
        # self.fleet_direction = 1 - движение пришельцев вправо по оси y, -1 - движение пришельцев влево
        self.fleet_direction = 1

        self.bullet_width = 2
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 3
        self.bullets_limit = 4

        self.drop_color = (255, 0, 0)
        self.drop_width = 5
        self.drop_height = randint(10, 80)
        self.drop_speed = 3
        self.drop_wind = 0

