
class GameStats():
    """Класс для ведения статистики игровой сессии"""

    def __init__(self, ai_game):
        """Инициализация статистики игры"""

        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Инициализация статистики, изменяющейся в ходе игры"""

        self.ships_left = self.settings.ship_limit


