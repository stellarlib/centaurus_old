from random import randint


def vary_color((r, g, b), variance):

    v = variance

    r += randint(-v, v)
    g += randint(-v, v)
    b += randint(-v, v)

    r = max(min((r, 255)), 0)
    g = max(min((g, 255)), 0)
    b = max(min((b, 255)), 0)

    return r, g, b
