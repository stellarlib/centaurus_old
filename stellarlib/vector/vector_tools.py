from vector import Vector
from math import sin, cos, radians


def get_line_segment(v1, v2, portion):

    portion = float(portion)
    assert 0.0 <= portion <= 1.0

    seg = Vector(v2.get_sub_tuple(v1))
    seg.mult(portion)
    seg.add(v1)

    return seg


def get_vertex_names(vertices):

    a = ord('a')
    names = []

    for i in range(len(vertices)):
        names.append(chr(a))
        a += 1

    return names


# input ordered list, returns list of corner sequences
def get_corner_sequences(names):

    corners = []

    l = len(names)
    for i in range(l):

        corners.append(tuple(names[:3]))
        front = names.pop(0)
        names.append(front)

    return corners


# input ordered list, return list of edge pairs
def get_edge_sequences(names):

    edges = []

    l = len(names)
    for i in range(l):

        j = i + 1
        if j == l:
            j = 0

        edges.append((names[i], names[j]))

    return edges


def get_cut_off_corner(corner_key, shape, corner_sequence, cutoff_gap, corner_length):

    A = shape[corner_sequence[0]]
    B = shape[corner_sequence[1]]
    C = shape[corner_sequence[2]]

    c_vertices = {}
    c_sequence = []

    d = get_line_segment(B, A, cutoff_gap)
    e = get_line_segment(B, C, cutoff_gap)
    f = get_line_segment(d, A, corner_length)
    g = get_line_segment(e, C, corner_length)

    # .     B
    # .   d   e
    # .  f     g
    # .A         C

    verts = [f, d, e, g]
    ids = ('f', 'd', 'e', 'g')

    for i in range(4):

        vert_id = '_'.join((corner_key, ids[i]))
        c_vertices[vert_id] = verts[i]
        c_sequence.append(vert_id)

    return c_vertices, c_sequence


def cut_off_corners_of_shape(shape, cutoff_gap, corner_length):

    corners = []

    v_names = get_vertex_names(shape)
    corner_sequences = get_corner_sequences(v_names)

    i = 0
    for seq in corner_sequences:

        k = '.'.join(('ccorn', v_names[i]))
        corners.append(get_cut_off_corner(k, shape, seq, cutoff_gap, corner_length))
        i += 1

    return corners


def get_line_angle(A, B):
    return Vector(A.get_sub_tuple(B)).get_angle()


def get_beveled_line_inset(key, A, B, base_inset, rect_inset, bevel_angle, bevel_height):

    # A   a---b      e---d   B
    #          \    /
    #           c--f

    a = get_line_segment(A, B, base_inset)
    d = get_line_segment(B, A, base_inset)

    b = get_line_segment(a, B, rect_inset)
    e = get_line_segment(d, A, rect_inset)

    # angle of the line we are insetting
    line_angle = get_line_angle(b, a)

    c = Vector.from_angle(-bevel_angle+line_angle, bevel_height)
    c.add(b)

    line_angle = line_angle - 360.0

    f = Vector.from_angle(-180+bevel_angle+line_angle, bevel_height)
    f.add(e)

    verts = [a, b, c, f, e, d]
    ids = ('a', 'b', 'c', 'f', 'e', 'd')

    b_vertices = {}
    b_sequence = []

    for i in range(6):

        vert_id = '.'.join((key, ids[i]))
        b_vertices[vert_id] = verts[i]
        b_sequence.append(vert_id)

    return b_vertices, b_sequence


def get_pair_hash_marks(key, A, B, spacing, width, height):

    hashes = []

    spaces = [-spacing/2, spacing/2]

    for i in range(len(spaces)):

        k = '.'.join((key, str(i)))
        hash = get_hash_mark(k, A, B, .5 + spaces[i], width, height)

        hashes.append(hash)

    return hashes


def get_hash_mark(key, A, B, pos, width, height):

    base = get_line_segment(A, B, pos)

    line_angle = get_line_angle(A, B)
    angle_unit = Vector.from_angle(line_angle, 1)

    #  a-b
    #  \ /
    #   c

    w = Vector(angle_unit)
    w.mult(width)

    a = Vector(w)
    a.add(base)

    b = Vector(w)
    b.mult(-1)
    b.add(base)

    c = Vector.from_angle(line_angle - 90, -1)
    c.mult(height)

    c.add(base)

    verts = [a, b, c]
    ids = ('a', 'b', 'c')

    vertices = {}
    sequence = []

    for i in range(3):

        vert_id = '.'.join((key, ids[i]))
        vertices[vert_id] = verts[i]
        sequence.append(vert_id)

    return vertices, sequence

