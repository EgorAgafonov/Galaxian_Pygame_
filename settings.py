import pygame

"""Класс с настройками игры Alien_Invasion"""


class Settings:
    def __init__(self):
        """Инициализируем настройки игры"""

        self.background_color = (4, 2, 80)
        self.background_image = pygame.image.load('images/background_screen.png')
        self.screen_width = self.background_image.get_width()
        self.screen_height = self.background_image.get_height()

        self.meteor_speed = 3
        self.ship_speed = 3
        self.alien_speed = 2.0

        self.fleet_drop_speed = 20
        # self.fleet_direction = 1 - движение пришельцев вправо по оси y, -1 - движение пришельцев влево
        self.fleet_direction = 1

        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 8
        self.bullets_limit = 4

        self.drop_color = (255, 0, 0)
        self.drop_width = 5
        self.drop_height = 60
        self.drop_speed = 10

