

class Burst(object):

    def __init__(self, number_shots, burst, inter_delay, post_delay, initial_delay=0, repeat=1):

        self.emitter = None
        self.number_shots = number_shots

        self.fire_pattern = self._create_fire_pattern(burst, inter_delay, post_delay, initial_delay, repeat)

        self.tick = 0
        self.duration = len(self.fire_pattern)

    def bind_emitter(self, emitter):
        self.emitter = emitter

    def update(self):

        self.tick += 1

        if self.tick >= self.duration:
            self.end()

    @property
    def firing(self):
        return self.fire_pattern[self.tick] > 0

    @property
    def final_shot(self):
        return self.fire_pattern[self.tick] == 2

    def end(self):
        self.emitter.mark_complete()

    def _create_fire_pattern(self, burst, inter_delay, post_delay, initial_delay, repeat):

        fire_pattern = []

        _initial_delay = [0] * initial_delay

        _burst = []
        for b in range(burst-1):
            _burst.append(1)
            _inter_delay = [0] * inter_delay
            _burst.extend(_inter_delay)
        _burst.append(1)

        _post_delay = [0] * post_delay
        _burst.extend(_post_delay)

        _sequence = _burst * repeat

        fire_pattern.extend(_initial_delay)
        fire_pattern.extend(_sequence)

        for i in range(len(fire_pattern)):

            if fire_pattern[-1-i] == 1:
                fire_pattern[-1-i] = 2
                break

        return fire_pattern
