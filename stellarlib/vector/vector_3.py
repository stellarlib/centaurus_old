import math


class Vector3(object):

    def __init__(self, *args):

        if isinstance(args[0], tuple) or isinstance(args[0], Vector3):
            x = args[0][0]
            y = args[0][1]
            z = args[0][2]
        else:
            x = args[0]
            y = args[1]
            z = args[2]

        if len(args) > 3:
            raise ValueError('Vector3 object can only have 3 elements')

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return str(self.get_tuple())

    def __getitem__(self, key):

        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise KeyError('Vector3 object has only 3 elements')

    def set(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @property
    def magnitude(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def get_inverse(self):
        inverse = Vector3(self)
        inverse.mult(-1)
        return inverse

    def get_unit_vector(self):
        mag = self.magnitude
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def get_tuple(self):

        return self.x, self.y, self.z

    def add(self, vec):

        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def sub(self, vec):

        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z

    def mult(self, scalar):

        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def div(self, scalar):

        self.x /= scalar
        self.y /= scalar
        self.z /= scalar

    # math functions that don't mutate the vector and return tuple
    def get_add_tuple(self, other, integer=False):
        x = self.x + other[0]
        y = self.y + other[1]
        z = self.z + other[2]
        if integer:
            return int(round(x)), int(round(y)), int(round(z))
        return x, y, z

    def get_sub_tuple(self, other, integer=False):
        x = self.x - other[0]
        y = self.y - other[1]
        z = self.z - other[2]
        if integer:
            return int(round(x)), int(round(y)), int(round(z))
        return x, y, z

    def get_mult_tuple(self, scalar, integer=False):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        if integer:
            return int(round(x)), int(round(y)), int(round(z))
        return x, y, z

    def get_div_tuple(self, scalar, integer=False):
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        if integer:
            return int(round(x)), int(round(y)), int(round(z))
        return x, y, z