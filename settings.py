"""Класс с настройками игры Alien_Invasion"""


class Settings:
    def __init__(self):
        """Инициализируем настройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (4, 2, 80)
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_limit = 4

