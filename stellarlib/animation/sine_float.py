from sine_motion import SineMotion


class SineFloat(SineMotion):

    def __init__(self, actor, amplitude, half_period=10):

        SineMotion.__init__(self, actor, amplitude, half_period=half_period)

    def wave_complete(self):
        self.tick = 0
