

# returns generator that will give all x, y pairs of an object with
# w and h fields
def all_points(area):

    return ((x, y) for x in range(area.w) for y in range(area.h))
