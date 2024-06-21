import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from allien import Alien
from raindrop import RainDrop
from random import randint


class AlienInvasion:
    def __init__(self):
        """Инициализируем игру и создаем игровые ресурсы."""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(screen=self.screen, ai_settings=self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()

        self._create_aliens_fleet()
        self._create_rainfall()

    def run_game(self):
        """Запуск основного цикла игры"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_rain_drops()
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

    def _update_rain_drops(self):
        """"""

        self.drops.update()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""

        self._check_fleet_edges()
        self.aliens.update()

    def _create_aliens_fleet(self):
        """Создание флота пришельцев"""

        # создание корабля пришельца и вычисление количества пришельцев в ряду
        # интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # определим количество рядов, помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
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

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_rainfall(self):
        """Создание стены дождевых капель"""

        # создание потока капель и вычисление количества дождевых потоков в ряду
        # интервал между дождевыми потоками равен высоте одного дождевого потока
        drop = RainDrop(self)
        drop_width = drop.rect.height
        available_space_x = self.settings.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)

        # создание первого ряда дожд. потока
        for drop_number in range(number_drops_x):
            self._create_drop(drop_number)

    def _create_drop(self, drop_number):
        """Создание одного дождевого потока, размещение его в ряду для последующего добавления в группу"""

        drop = RainDrop(self)
        #  задаем координату для размещения дождевого потока на оси x
        drop.x = randint(0, self.settings.screen_width) * drop_number
        drop.rect.x = drop.x
        self.drops.add(drop)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""

        self.screen.fill(self.settings.background_color)
        # self.screen.blit(self.settings.background_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.drops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
