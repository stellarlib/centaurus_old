

def lerp(start, end, t):

    if isinstance(start, int) or isinstance(start, float):
        return _lerp_single_value(start, end, t)
    elif isinstance(start, tuple):
        return _lerp_tuple(start, end, t)
    else:
        raise ValueError("Expected number or tuple values.")


def _lerp_single_value(start, end, t):

    delta = end - start

    return start + (delta * t)


def _lerp_tuple(start, end, t):

    try:
        assert len(start) == len(end)
    except AssertionError("Inputs must all be the same length."):
        pass

    lerped = []
    for i in range(len(start)):
        lerped.append(_lerp_single_value(start[i], end[i], t))

    return tuple(lerped)


def lerp_color(start, end, t):

    col = lerp(start, end, t)
    trimmed = []
    for c in col:

        c = int(max((min((c, 255)), 0)))

        trimmed.append(c)

    return tuple(trimmed)