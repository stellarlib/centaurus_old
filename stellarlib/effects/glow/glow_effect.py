from stellarlib.color import Color


class GlowEffect(object):

    min_alpha = 50
    max_alpha = 200

    transition_rate = 5

    def __init__(self, group, mask, color=Color.WHITE):

        self.group = group

        self.alpha = 100
        self.rate = GlowEffect.transition_rate

        self.sprite = mask
        self.sprite.change_color(color)

        self.group.add(self)

    def update(self):

        self.update_alpha()

        if self.effect_complete():
            self.end()

    def effect_complete(self):

        return False

    def end(self):

        self.group.mark_for_removal(self)

    def draw(self, surf):

        self.sprite.draw(surf)

    def update_alpha(self):

        self.alpha += self.rate

        if self.alpha > GlowEffect.max_alpha:

            self.alpha = GlowEffect.max_alpha
            self.rate *= -1

        elif self.alpha < GlowEffect.min_alpha:

            self.alpha = GlowEffect.min_alpha
            self.rate *= -1

        self.sprite.set_alpha(self.alpha)
