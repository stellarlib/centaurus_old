

# returns if point in bounds of area with w and h
def in_bounds(area, (x, y)):

    return 0 <= x < area.w and 0 <= y < area.h


def get_adj(area, (x, y), diag=False):
    adj = _get_adj((x, y), diag=diag)
    return filter(lambda p: in_bounds(area, p), adj)


def _get_adj((x, y), diag=False):
    adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    if diag:
        adj.extend([(x + 1, y + 1), (x - 1, y - 1),
                    (x - 1, y + 1), (x - 1, y - 1)])
    return adj


def get_edge(collection):

    edge = set()
    members = set(collection)

    for point in collection:

        adj = _get_adj(point)

        for a in adj:
            if a not in members:
                edge.add(point)
                break

    return edge
