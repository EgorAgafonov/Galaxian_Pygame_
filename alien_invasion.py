import sys
import pygame


class AlienInvasion:
    def __init__(self):
        """Инициализируем игру и создаем игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (173, 216, 230)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
