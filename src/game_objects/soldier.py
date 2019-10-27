from enemy import Enemy
from src.game.logic.ai_control.unit_ai import BaseAI


class Soldier(Enemy):

    def __init__(self, game, pos):

        Enemy.__init__(self, game, 'soldier', pos)

    def _load_ai(self):
        return BaseAI(self)
