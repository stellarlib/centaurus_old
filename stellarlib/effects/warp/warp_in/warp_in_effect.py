import pygame

from stellarlib.effects.warp.warp_in_lerp import WarpInLerp
from stellarlib.map_tools import all_points
from stellarlib.particles import Group, WarpInParticle, GateParticleEffect
from stellarlib.settings import PIXEL_SCALE


class WarpInEffect(object):

    interval = 6
    colorkey = (255, 0, 255)

    def __init__(self, sprite, resolve_func):

        self.sprite = sprite
        self.resolve_func = resolve_func

        self.group = self.sprite.effects
        self.silhouette = self.sprite.silhouette
        self.x_flip = self.sprite._flipped_silhouette

        # create warp sequence
        self.warp_sequence = self.compute_warp_sequence()
        self.gate_size = self.compute_gate_size()
        self.sprite_length = len(self.warp_sequence)
        self.warp_lerp = WarpInLerp(self, WarpInEffect.interval)

        # create particle Group
        self.particles = Group()

        # follow the sequence adding particles to the group
        self.tick = 0
        self.effect_surface = self.init_effect_surface()

        self.group.add(self)

        self.initialize_effect()
        self.create_gate_particle()

    def initialize_effect(self):

        self.sprite.image.hide()

    def deinitialize_effect(self):

        self.sprite.image.show()
        if self.resolve_func:
            self.resolve_func()

    def init_effect_surface(self):
        i = pygame.Surface((self.silhouette.w * PIXEL_SCALE, self.silhouette.h * PIXEL_SCALE))
        i.fill(WarpInEffect.colorkey)
        i.set_colorkey(WarpInEffect.colorkey)
        return i

    def update(self):

        if self.tick == 0 and self.warp_sequence:
            self.add_warp_particle_column()

        self.particles.update()

        self.run_warp_lerp()
        self.tick -= 1

        if self.effect_complete():
            self.end()
            self.deinitialize_effect()

    def add_warp_particle_column(self):

        points = self.warp_sequence.pop(0)

        for x, y in points:
            self.add_warp_particle(x, y)

        self.tick += WarpInEffect.interval

    def effect_complete(self):
        return self.particles.empty() and not self.warp_sequence

    def end(self):
        self.group.mark_for_removal(self)

    def add_warp_particle(self, x, y):

        px = x * PIXEL_SCALE
        py = y * PIXEL_SCALE

        col = self.sprite.image.get_pixel_color(px, py)
        if col == (255, 255, 255):
            return

        if self.x_flip:
            px = self.flip_x(x) * PIXEL_SCALE

        WarpInParticle(self.particles, (px, py), col)

    def draw(self, surf, rel_pos):

        self.particles.draw(self.effect_surface, (0, 0))

        x, y = self.warp_lerp.get_coord(rel_pos)

        surf.surface.blit(self.effect_surface, (x, y))

    def compute_warp_sequence(self):

        silhouette_points = set(filter(lambda (x, y): self.silhouette.get_cell(x, y), all_points(self.silhouette)))

        # add empty buffer to allow gate to open first
        sequence = [[]]*(GateParticleEffect.opening_duration/WarpInEffect.interval)
        x = 0

        while silhouette_points:

            column = filter(lambda point: point[0] == x, silhouette_points)

            if column:
                sequence.append(column)

                silhouette_points.difference_update(column)

            x += 1

        return sequence

    def run_warp_lerp(self):

        self.warp_lerp.run()

    def flip_x(self, x):
        return self.silhouette.w - x - 1

    def compute_gate_size(self):
        column_heights = [len(s) for s in self.warp_sequence]
        return max(column_heights)

    def create_gate_particle(self):

        sil_w = self.silhouette.w / 2 * PIXEL_SCALE

        gate_duration = WarpInEffect.interval * len(self.warp_sequence) + \
                        GateParticleEffect.opening_duration / WarpInEffect.interval

        # we place the gate at the x of the final column in the warp sequence
        gate_x = self.warp_sequence[-1][0][0] + 1
        if self.x_flip:
            gate_x = self.flip_x(gate_x) - 2

        gate_x = gate_x * PIXEL_SCALE - sil_w + PIXEL_SCALE

        GateParticleEffect(self.group, (gate_x, 0), self.gate_size, gate_duration)

