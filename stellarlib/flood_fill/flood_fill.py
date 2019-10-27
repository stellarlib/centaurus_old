

# returns an edge n layers flooded from the start edge
def flood_range(start_edge, valid_func, n):

    edge = set(start_edge)
    touched_set = set(start_edge)

    for i in range(n):

        edge = flood(edge, valid_func, touched_set)
        touched_set.update(edge)

    return edge


# returns a flooded area from a start edge
# option arg n is a limit on number of iterations
def flood_fill(start_edge, valid_func, n=-1):

    edge = set(start_edge)
    touched_set = set(start_edge)

    i = n

    while edge:

        edge = flood(edge, valid_func, touched_set)
        touched_set.update(edge)

        i -= 1
        if i == 0:
            break

    return touched_set


def flood(edge, valid_func, touched_set):

    new_edge = set()

    for point in edge:
        add_neighbours(point, new_edge, valid_func, touched_set)

    return new_edge


def add_neighbours(point, edge, valid_func, touched_set):
    for adj_point in get_adj(point, valid_func, touched_set):
        edge.add(adj_point)


def get_adj((x, y), valid_func, touched_set):
    adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    return filter(lambda p: point_is_valid(p, valid_func, touched_set), adj)


def point_is_valid(point, valid_func, touched_set):

    if point in touched_set:
        return False
    return valid_func(point)
