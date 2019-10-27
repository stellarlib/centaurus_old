from stellarlib.flood_fill import flood
from stellarlib.map_tools import in_bounds
from stellarlib.particles import Group, ShieldFlash
from random import random, randint
from stellarlib.settings import PIXEL_SCALE
from stellarlib.color import BeamColors


class ShieldSplashEffect(object):

    interval = 2
    noise = 0.3
    min_size = 10
    max_size = 16

    edge_latency = 10

    def __init__(self, sprite, origin, color=(10, 230, 240)):

        self.sprite = sprite
        self.group = self.sprite.effects
        self.silhouette = self.sprite.shielded_silhouette
        self.x_flipped = self.sprite._flipped_silhouette

        self.color_palette = BeamColors(color)
        self.delay = ShieldSplashEffect.interval

        # create splash sequence
        self.splash_sequence = self.compute_splash_seqeunce(self.silhouette, origin)

        # if effect needs to be mirrored, flip x coords
        if self.x_flipped:
            self.flip_splash_sequence()

        # create particle Group
        self.splash = Group()

        # follow the sequence adding particles to the group
        self.tick = 0

        self.group.add(self)

    def update(self):

        if self.tick == 0 and self.splash_sequence:

            points = self.splash_sequence.pop(0)

            for x, y in points:

                self.add_shield_particle(x, y)

            self.tick += ShieldSplashEffect.interval

        self.splash.update()
        self.tick -= 1
        if self.effect_complete():
            self.end()

    def effect_complete(self):
        return self.splash.empty() and not self.splash_sequence

    def end(self):
        self.group.mark_for_removal(self)

    def add_shield_particle(self, x, y):

        px = (x - self.silhouette.w / 2) * PIXEL_SCALE
        py = (y - self.silhouette.h / 2) * PIXEL_SCALE

        sf = ShieldFlash(self.splash, (px, py), self.color_palette)

        if self.x_flipped:
            x = self.flip_x(x)

        if (x, y) in self.silhouette.edge:
            sf.duration += ShieldSplashEffect.edge_latency

    def draw(self, surf, rel_point):

        self.splash.draw(surf, rel_point)

    def compute_splash_seqeunce(self, silhouette, origin):

        sequence = []

        edge = {origin}
        touched_set = {origin}

        sequence.append(edge)

        def valid((x, y)):
            return in_bounds(silhouette, (x, y)) and silhouette.get_cell(x, y)

        if not valid(origin):
            return []

        for i in range(randint(ShieldSplashEffect.min_size, ShieldSplashEffect.max_size)):

            edge = flood(edge, valid, touched_set)
            edge = self.apply_noise_to_edge(edge)
            touched_set.update(edge)

            sequence.append(edge)

        return sequence

    def apply_noise_to_edge(self, edge):

        def remove_point(point):

            if point in self.silhouette.edge:
                return True
            else:
                return random() > ShieldSplashEffect.noise

        return filter(remove_point, edge)

    def flip_splash_sequence(self):

        new_splash_seq = []

        for edge in self.splash_sequence:
            new_edge = set()
            for x, y in edge:

                nx = self.flip_x(x)
                new_edge.add((nx, y))

            new_splash_seq.append(new_edge)

        self.splash_sequence = new_splash_seq

    def flip_x(self, x):
        return self.silhouette.w - x - 1
