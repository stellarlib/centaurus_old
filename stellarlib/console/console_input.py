from pygame.locals import *


class ConsoleInput(object):

    strike_delay = 15
    hold_delay = 4

    def __init__(self, console):

        self.console = console

        self.shift_down = False
        self.backspace_down = False

        self.keys = self._init_keys()

        self.strike = False
        self.tick = 0

    @property
    def _keys(self):
        return self.console._keys

    @property
    def _shift_keys(self):
        return self.console._shift_keys

    def handle_input(self, event):
        if event.type == KEYDOWN:

            if event.key in self._keys:
                self.press_key(event.key)
            elif event.key == K_BACKSPACE:
                self.backspace_down = True
            elif event.key == K_RETURN:
                self.console.run_prompt()
            elif event.key in (K_LSHIFT, K_RSHIFT):
                self.shift_down = True
            elif event.key == K_UP:
                self.console.line_cursor_up()
                self.console.grab_line()
            elif event.key == K_DOWN:
                self.console.line_cursor_down()
                self.console.grab_line()
            self.strike = True

        elif event.type == KEYUP:
            if event.key in self.console._keys:
                self.release_key(event.key)
            elif event.key == K_BACKSPACE:
                self.backspace_down = False
            elif event.key in (K_LSHIFT, K_RSHIFT):
                self.shift_down = False

    def update(self):

        if self.strike:
            self.key_strike()
            self.strike = False
            self.tick += self.strike_delay
        elif self.tick == 0:
            self.key_strike()
            self.tick += self.hold_delay

        if self.tick > 0:
            self.tick -= 1

    def key_strike(self):
        for k in self.console._iter_keys:
            if self.keys[k]:
                self.trigger_key(k)

        if self.backspace_down:
            self.console._backspace()

    def trigger_key(self, k):

        if self.shift_down and k in self._shift_keys:
            char = self._shift_keys[k]
        else:
            char = self._keys[k]
        self.console._keystroke(char)

    def reset(self):
        self.shift_down = False
        self.backspace_down = False
        for k in self.console._iter_keys:
            self.keys[k] = False

    def press_key(self, k):
        self.keys[k] = True

    def release_key(self, k):
        self.keys[k] = False

    def _init_keys(self):

        keys = {k: False for k in self._keys.keys()}

        return keys
