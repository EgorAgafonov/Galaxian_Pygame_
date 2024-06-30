"""Класс с настройками игры Alien_Invasion"""
import pygame
from random import randint


class Settings:
    def __init__(self):
        """Инициализируем настройки игры"""

        # DISPLAY
        self.background_color = (4, 2, 80)
        self.background_image = pygame.image.load('images/background_screen.png')
        self.screen_width = self.background_image.get_width()
        self.screen_height = self.background_image.get_height()

        # SHIP
        self.ship_limit = 3
        self.ship_speed = 6

        # ALIENS
        self.fleet_drop_speed = 20
        # self.fleet_direction = 1 - движение пришельцев вправо по оси x, -1 - движение пришельцев влево
        self.fleet_direction = 1
        self.alien_speed = 4

        # BULLET
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_limit = 4
        self.bullet_speed = 18

        # RAIN DROP
        self.drop_color = (255, 0, 0)
        self.drop_width = 5
        self.drop_height = 0
        self.drop_wind = 0
        self.drop_speed = 20

