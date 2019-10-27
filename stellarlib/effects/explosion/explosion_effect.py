from stellarlib.flood_fill import flood
from stellarlib.particles import Group, ExplosionParticle
from random import random, randint
from stellarlib.settings import PIXEL_SCALE
from stellarlib.color import ExplosionColors


class ExplosionEffect(object):

    interval = 3
    noise = 0.4
    min_size = 5
    max_size = 8

    min_particles = 6

    def __init__(self, group, silhouette, origin, x_flipped):

        self.group = group
        self.color_palette = ExplosionColors()
        self.delay = ExplosionEffect.interval
        self.silhouette = silhouette
        self.x_flipped = x_flipped

        # create sequence
        self.explosion_sequence = self.compute_explosion_sequence(origin)

        # if effect needs to be mirrored, flip x coords
        if x_flipped:
            self.flip_explosion_sequence()

        # create particle Group
        self.burst = Group()

        # follow the sequence adding particles to the group
        self.tick = 0
        self.stage = 1

        self.group.add(self)

    def update(self):

        if self.tick == 0 and self.explosion_sequence:

            points = self.explosion_sequence.pop(0)
            for x, y in points:
                self.add_explosion_particle(x, y, self.stage)
            self.tick += ExplosionEffect.interval
            self.stage += 1

        self.burst.update()
        self.tick -= 1

        if self.effect_complete():
            self.end()

    def effect_complete(self):
        return self.burst.empty() and not self.explosion_sequence

    def end(self):
        self.group.mark_for_removal(self)

    def add_explosion_particle(self, x, y, stage):

        px = (x - self.silhouette.w / 2) * PIXEL_SCALE
        py = (y - self.silhouette.h / 2) * PIXEL_SCALE

        ExplosionParticle(self.burst, (px, py), self.color_palette, stage)

    def draw(self, surf, rel_pos):

        self.burst.draw(surf, rel_pos)

    def compute_explosion_sequence(self, origin):

        origin = self.sanitize_origin_input(origin)

        sequence = []

        edge = set(origin)
        touched_set = set(origin)

        sequence.append(edge)

        size = randint(ExplosionEffect.min_size, ExplosionEffect.max_size)

        for i in range(size):

            edge = flood(edge, lambda x: True, touched_set)
            edge = filter(lambda x: random() > ExplosionEffect.noise, edge)

            if i == size / 2 or len(edge) < ExplosionEffect.min_particles:
                self.extend_burst(edge, touched_set)

            touched_set.update(edge)

            sequence.append(edge)

        return sequence

    def extend_burst(self, edge, touched):

        extended = touched.difference(edge)

        edge.extend(extended)

    def sanitize_origin_input(self, origin):

        if isinstance(origin, tuple):
            return [origin]
        return origin

    def flip_explosion_sequence(self):

        new_explosion_seq = []

        for edge in self.explosion_sequence:
            new_edge = set()
            for x, y in edge:

                nx = self.flip_x(x)
                new_edge.add((nx, y))

            new_explosion_seq.append(new_edge)

        self.explosion_sequence = new_explosion_seq

    def flip_x(self, x):
        return self.silhouette.w - x - 1

