from particle import Particle
from stellarlib.settings import PIXEL_SCALE
import pygame
from random import randint
from stellarlib.lerp.lerp import lerp, lerp_color
from stellarlib.color import Color, vary_color


class GateParticleEffect(Particle):

    rect = pygame.Rect((0, 0), (PIXEL_SCALE, PIXEL_SCALE))

    opening_duration = 20
    gate_extension = 8
    color_variance = 20
    fluctuation_range = 4
    core_offset = 3

    OPENING = 0
    HOLDING = 1
    CLOSING = 2

    stages = (OPENING, HOLDING, CLOSING)

    def __init__(self, group, (x, y), height, duration, shimmer_color=(100, 150, 250)):

        Particle.__init__(self, group, (x, y))

        self.points = [(0, 0)]
        self.stage = GateParticleEffect.OPENING
        self.tick = 0

        self.height = height + GateParticleEffect.gate_extension
        self.open_duration = duration + GateParticleEffect.opening_duration
        self.full_duration = duration + GateParticleEffect.opening_duration * 2

        self.shimmer_color = shimmer_color

    def on_update(self):

        cls = GateParticleEffect
        if self.tick > self.open_duration:
            self.stage = cls.CLOSING
        elif self.tick > cls.opening_duration:
            self.stage = cls.HOLDING

        self.tick += 1

        if self.stage == cls.OPENING:
            self.open_aperture()

        elif self.stage == cls.CLOSING:
            self.close_aperture()

    def check_end_condition(self):
        return self.tick > self.full_duration

    def draw(self, surface, (rx, ry)):

        sx, sy = self.coord.get_tuple_int()
        x = sx + rx
        y = sy + ry

        flux = randint(0, GateParticleEffect.fluctuation_range)
        for px, py in self.points:
            self.draw_point(surface.surface, (px, py), (x, y), flux)

        top_y = self.points[-1][1]
        for i in range(flux):

            fy = top_y + i
            self.draw_point(surface.surface, (0, fy), (x, y), flux)

    def draw_point(self, surface, (x, y), (rx, ry), flux, core=True, noise=True):

        px = x * PIXEL_SCALE
        py = y * PIXEL_SCALE

        # lower_point
        cls = GateParticleEffect
        cls.rect.topleft = px + rx, py + ry
        pygame.draw.rect(surface, self.fluctuate_point_color(py), cls.rect)

        # upper point
        cls.rect.topleft = px + rx, -py + ry
        pygame.draw.rect(surface, self.fluctuate_point_color(py), cls.rect)

        if abs(y) < self.height/2-GateParticleEffect.core_offset + flux and core:
            self.draw_point(surface, (x-1, y), (rx, ry), flux, core=False, noise=True)
            self.draw_point(surface, (x+1, y), (rx, ry), flux, core=False, noise=True)

        elif noise:

            y_weight = abs(py/PIXEL_SCALE)
            noise_chance = y_weight*2 + 1

            if randint(0, noise_chance) == 0:
                self.draw_point(surface, (x-1, y), (rx, ry), flux, core=False, noise=False)
            if randint(0, noise_chance) == 0:
                self.draw_point(surface, (x+1, y), (rx, ry), flux, core=False, noise=False)

    def fluctuate_point_color(self, y):

        t = y / float(self.height) / 2
        base_col = lerp_color(Color.WHITE, self.shimmer_color, t)

        return vary_color(base_col, GateParticleEffect.color_variance)

    def open_aperture(self):

        t = self.tick / float(self.opening_duration)
        l = int(round(lerp(0, self.height/2.0, t)))

        edge_y = self.points[-1][1]

        while edge_y < l:

            edge_y += 1
            self.points.append((0, edge_y))

    def close_aperture(self):

        t = (self.tick - self.open_duration) / float(self.opening_duration)
        l = int(round(lerp(self.height / 2.0, 0, t)))

        edge_y = self.points[-1][1]

        while edge_y > l > 0:
            self.points.pop()
            edge_y = self.points[-1][1]
