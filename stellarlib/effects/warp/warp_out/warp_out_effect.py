import pygame

from stellarlib.effects.warp.warp_out_lerp import WarpOutLerp
from stellarlib.map_tools import all_points
from stellarlib.particles import GateParticleEffect, Group
from stellarlib.settings import PIXEL_SCALE


class WarpOutEffect(object):

    interval = 6
    colorkey = (255, 0, 255)

    def __init__(self, sprite, resolve_func=None):

        self.sprite = sprite
        self.resolve_func = resolve_func

        self.group = self.sprite.effects
        self.silhouette = self.sprite.silhouette
        self.x_flip = self.sprite._flipped_silhouette

        # create warp sequence
        self.column_range, self.gate_size = self.compute_column_range_and_gate_size()
        self.sprite_length = self.column_range[1] - self.column_range[0]
        self.warp_lerp = WarpOutLerp(self, WarpOutEffect.interval)

        # follow the sequence adding particles to the group
        self.tick = GateParticleEffect.opening_duration
        self.col = 0
        self.effect_surface = self.init_effect_surface()
        self.column_rect = self.init_column_rect()

        self.gate_open = False

        self.particle = Group()
        self.group.add(self)

        self.initialize_effect()
        self.create_gate_particle()

    def initialize_effect(self):

        self.sprite.image.hide()

    def init_effect_surface(self):
        i = pygame.Surface((self.silhouette.w * PIXEL_SCALE, self.silhouette.h * PIXEL_SCALE))
        i.fill(WarpOutEffect.colorkey)
        i.set_colorkey(WarpOutEffect.colorkey)

        x = self.silhouette.w*PIXEL_SCALE / 2
        y = self.silhouette.h*PIXEL_SCALE / 2

        self.sprite.image.force_draw(i, (x, y))

        return i

    def init_column_rect(self):
        return pygame.Rect((0, 0), (1*PIXEL_SCALE, self.silhouette.h*PIXEL_SCALE))

    def update(self):

        if self.gate_open:
            self.move_ship()
        else:
            self.tick -= 1
            if self.tick == 0:
                self.gate_open = True

        self.particle.update()

        if self.effect_complete():
            self.end()

    def move_ship(self):

        if self.tick == 0:
            self.erase_column()
            self.col += 1

        self.run_warp_lerp()
        self.tick -= 1

    def erase_column(self):

        x = self.col

        if self.x_flip:
            x = self.flip_x(x)

        self.column_rect.topleft = (x * PIXEL_SCALE, 0)
        pygame.draw.rect(self.effect_surface, WarpOutEffect.colorkey, self.column_rect)

        self.tick += WarpOutEffect.interval

    def effect_complete(self):
        return self.particle.empty()

    def end(self):
        self.group.mark_for_removal(self)
        self.on_complete()

    def draw(self, surf, rel_pos):

        x, y = self.warp_lerp.get_coord(rel_pos)

        surf.surface.blit(self.effect_surface, (x, y))
        self.particle.draw(surf, rel_pos)

    def compute_column_range_and_gate_size(self):

        silhouette_points = set(filter(lambda (x, y): self.silhouette.get_cell(x, y), all_points(self.silhouette)))

        x = 0
        start_col = -1
        col = 0

        gate_size = 0

        for x in range(self.silhouette.w):

            column_points = filter(lambda point: point[0] == x, silhouette_points)

            if column_points:
                if start_col == -1:
                    start_col = x

                col += 1
                if len(column_points) > gate_size:
                    gate_size = len(column_points)

        end_col = start_col + col

        column_range = (start_col, end_col)

        return column_range, gate_size

    def run_warp_lerp(self):

        if self.col > self.column_range[0]:

            self.warp_lerp.run()

    def flip_x(self, x):
        return self.silhouette.w - x - 1

    def compute_gate_size(self):
        column_heights = [len(s) for s in self.warp_sequence]
        return max(column_heights)

    def create_gate_particle(self):

        sil_w = (self.silhouette.w / 2) * PIXEL_SCALE

        gate_duration = WarpOutEffect.interval * self.column_range[1] + GateParticleEffect.opening_duration

        # we place the gate at the x of the first column in the warp sequence
        gate_x = self.column_range[0] - 2
        if self.x_flip:
            gate_x = self.flip_x(gate_x) - 2

        gate_x = gate_x * PIXEL_SCALE - sil_w + PIXEL_SCALE

        GateParticleEffect(self.particle, (gate_x, 0), self.gate_size, gate_duration)

    def on_complete(self):
        if self.resolve_func:
            self.resolve_func()
