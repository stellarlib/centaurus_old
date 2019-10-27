from standard_control import StandardControl
from action_cost import *


class PlayerControl(object):

    STD = 0
    THROW = 1
    JUMP = 2
    CHARGE = 3

    str_to_enum = {
        'std': STD,
        'throw': THROW,
        'jump': JUMP,
        'charge': CHARGE,
    }

    def __init__(self, logic):

        self.game = logic.game
        self.logic = logic

        cls = PlayerControl
        self.mode = cls.STD

        self.controls = {
            cls.STD: StandardControl(self),
            cls.THROW: StandardControl(self),
            cls.JUMP: StandardControl(self),
            cls.CHARGE: StandardControl(self)
        }

        self._player_turn = True
        self._animating = False

    @property
    def player(self):
        return self.logic.player

    @property
    def active(self):
        return self._player_turn and not self._animating

    def switch_mode(self, key):

        # TODO check if we have enough action points to use the chosen mode

        cls = PlayerControl
        if self.mode == cls.str_to_enum[key]:
            self.mode = cls.STD
        else:
            self.mode = cls.str_to_enum[key]

    def handle_click(self, pos):
        if self.active:
            self.controls[self.mode].handle_click(pos)

    def move_player(self, pos):

        def resolve_func():
            self.spend_action(MOVE_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_move(pos, resolve_func)

    def player_attacks(self, pos):
        foe = self.logic.get_actor_at(pos)
        assert foe != self.player
        self.player.melee_attack(foe)
        self.spend_action(MELEE_COST)

    def player_throw_attacks(self, pos):
        foe = self.logic.get_actor_at(pos)
        assert foe != self.player
        self.player.range_attack(foe)
        self.spend_action(THROW_COST)

    def spend_action(self, x):

        self.switch_mode('std')

        assert x <= self.player.actions
        self.player.spend_actions(x)
        if self.player.actions == 0:
            self.end_turn()

    def start_player_turn(self):
        self._player_turn = True
        self.set_up_turn()

    def set_up_turn(self):
        self.player.restore(2)

    def tear_down_turn(self):

        print 'player turn over'
        self.logic.start_ai_turn()

    def end_turn(self):
        self.tear_down_turn()
        self._player_turn = False

    def rest(self):
        self.player.restore(1)
        self.end_turn()

    def manual_turn_end(self):
        if self.active:
            self.rest()

    def manual_switch_mode(self, mode):
        if self.active:
            self.switch_mode(mode)

    def start_animating(self):
        self._animating = True

    def end_animating(self):
        self._animating = False
