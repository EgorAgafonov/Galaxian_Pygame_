import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from allien import Alien


class AlienInvasion:
    def __init__(self):
        """Инициализируем игру и создаем игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(screen=self.screen, ai_settings=self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на событие нажатия клавиши вниз (KEYDOWN)"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на событие возвращения клавиши вверх (KEYUP)"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""

        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновление позиции снарядов и удаление старых снарядов"""

        # обновление позиции снарядов
        self.bullets.update()
        # удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def create_fleet(self):
        """Создание флота пришельцев"""

        # создание корабля пришельца и вычисление количества пришельцев в ряду
        # интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # определим количество рядов, помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # создание флота кораблей пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение в ряду"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
