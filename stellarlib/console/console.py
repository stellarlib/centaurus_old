from pygame.locals import *
from stellarlib.settings import SCREEN_W
from console_image import ConsoleImage
from prompt_image import PromptImage
from line_builder import LineBuilder
from char_image import CharImage
from stellarlib.color import Color
from command_evaluator import CommandEvaluator
from console_input import ConsoleInput


class Console(object):

    _keys = {
        K_a: 'a',
        K_b: 'b',
        K_c: 'c',
        K_d: 'd',
        K_e: 'e',
        K_f: 'f',
        K_g: 'g',
        K_h: 'h',
        K_i: 'i',
        K_j: 'j',
        K_k: 'k',
        K_l: 'l',
        K_m: 'm',
        K_n: 'n',
        K_o: 'o',
        K_p: 'p',
        K_q: 'q',
        K_r: 'r',
        K_s: 's',
        K_t: 't',
        K_u: 'u',
        K_v: 'v',
        K_w: 'w',
        K_x: 'x',
        K_y: 'y',
        K_z: 'z',
        K_0: '0',
        K_1: '1',
        K_2: '2',
        K_3: '3',
        K_4: '4',
        K_5: '5',
        K_6: '6',
        K_7: '7',
        K_8: '8',
        K_9: '9',
        K_SPACE: ' ',
        K_PERIOD: '.',
        K_MINUS: '-',
        K_COMMA: ',',
        K_LEFTBRACKET: '[',
        K_RIGHTBRACKET: ']',
        K_COLON: ';',
        K_QUOTE: "'",
    }

    _shift_keys = {
        K_9: '(',
        K_0: ')',
        K_MINUS: '_',
        K_COMMA: '<',
        K_PERIOD: '>',
        K_COLON: ':',
    }

    _iter_keys = [k for k in _keys.keys()]

    num_lines = 10
    max_line_len = (SCREEN_W / CharImage.w) - 1

    color_back = Color.BLACK
    def_color = Color.WHITE
    alpha = 200

    max_lines = 256

    def __init__(self):

        self.lines = []
        self.inputs = []
        self.prompt = []
        self.shown = False
        self.shift_down = False
        self.line_cursor = 0

        self.line_builder = LineBuilder(self)
        self.prompt_image = PromptImage(self)
        self.console_image = ConsoleImage(self)
        self.input_handler = ConsoleInput(self)

        self.evaluator = self._load_evaluator()

    def log(self, text, color=Color.WHITE):

        text = text.lower()

        overflow = None
        if len(text) > self.max_line_len:
            overflow = text[self.max_line_len:]
            text = text[:self.max_line_len]

        self._push_line(text)
        self.console_image.scroll()
        self.console_image.add_line(text, color)

        if overflow:
            self.log(overflow, color)

    def handle_input(self, event):

        if not self.shown:
            return

        self.input_handler.handle_input(event)

    def update(self):

        if not self.shown:
            return

        self.input_handler.update()

    def draw(self, surface, rel_pos):

        if not self.shown:
            return

        self.prompt_image.draw(surface)
        self.console_image.draw(surface)

    def show(self):
        self.shown = True
        self.shift_down = False

    def hide(self):
        self.shown = False
        self.input_handler.reset()

    def _load_evaluator(self):
        return CommandEvaluator(self)

    def _keystroke(self, char):

        if len(self.prompt) <= Console.max_line_len:
            self.prompt.append(char)
            self.prompt_image.keystroke(char, len(self.prompt))

    def _backspace(self):

        if self.prompt:
            self.prompt.pop()
            self.prompt_image.backspace(len(self.prompt) + 1)

    def _copy_line(self, line):
        del self.prompt[:]
        self.prompt_image.clear()
        for c in line:
            self._keystroke(c)

    def run_prompt(self):
        command = ''.join(self.prompt)
        self._push_prompt()
        self.evaluator.evaluate(command)

    def _push_prompt(self):

        # send text to console
        user_input = ''.join(self.prompt)
        self._log_user_input(user_input)
        self.log(user_input)
        del self.prompt[:]
        self.prompt_image.clear()

        self.line_cursor = 0

    def _push_line(self, text):

        self.lines.append(text)

        if len(self.lines) > self.max_lines:
            # TODO dump to file if necessary
            del self.lines[:]

    def line_cursor_up(self):
        self.line_cursor += 1
        self.line_cursor = min((self.line_cursor, len(self.inputs)))

    def line_cursor_down(self):
        self.line_cursor -= 1
        self.line_cursor = max((self.line_cursor, 1))

    def grab_line(self):
        if len(self.inputs) == 0:
            pass
        elif len(self.inputs) >= self.line_cursor:
            line = self.inputs[-self.line_cursor]
            self._copy_line(line)

    def _log_user_input(self, user_input):

        self.inputs.append(user_input)

        if len(self.inputs) > self.max_lines:
            # TODO dump to file if necessary
            del self.inputs[:]
