from stellarlib.effects.effect import Effect


class Emitter(Effect):

    def __init__(self, group, burst_pattern, create_particle_func):

        self.burst_pattern = burst_pattern
        self.particle_maker = create_particle_func

        self.complete = False

        Effect.__init__(self, group)

    def _on_update(self):
        if self.burst_pattern.firing:
            self.particle_maker(self.burst_pattern.final_shot)

        self.burst_pattern.update()

    def _initialize_effect(self):
        self.burst_pattern.bind_emitter(self)

    def effect_complete(self):
        return self.complete

    def mark_complete(self):
        self.complete = True
