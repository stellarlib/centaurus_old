from math import sin, cos, atan, radians, degrees, hypot


class Vector(object):

    # returns unit vector from given angle
    # optional length scalar will scale the vector
    @classmethod
    def from_angle(cls, angle_deg, scalar=None):
        th = radians(angle_deg)
        angle = cls(cos(th), sin(th))
        if scalar:
            angle.mult(scalar)

        return angle

    def __init__(self, *args):

        if not args:
            x = 0.0
            y = 0.0
        elif isinstance(args[0], tuple) or isinstance(args[0], Vector):
            x = args[0][0]
            y = args[0][1]
        else:
            x = args[0]
            y = args[1]

        if len(args) > 2:
            raise ValueError('Vector object can only have 2 elements')

        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return str(self.get_tuple())

    def __getitem__(self, key):

        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise KeyError('Vector object has only 2 elements')

    def set(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @property
    def magnitude(self):
        return hypot(self.x, self.y)

    def get_inverse(self):
        inverse = Vector(self)
        inverse.mult(-1)
        return inverse

    def get_angle(self):

        if self.x == 0:
            if self.y >= 0:
                return 90
            else:
                return 270

        angle = degrees(atan((self.y / self.x)))
        if self.x < 0:
            angle += 180
        return angle

    def get_tuple(self):
        return self.x, self.y

    def get_tuple_int(self):
        return int(round(self.x)), int(round(self.y))

    def match(self, vector):
        self.x = vector.x
        self.y = vector.y

    def get_unit_vector(self):
        return Vector(self.x / self.magnitude, self.y / self.magnitude)

    def set_at_angle(self, angle_deg):
        th = radians(angle_deg)
        length = self.magnitude
        self.set(cos(th), sin(th))
        self.mult(length)

    # mutative math functions
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    # math functions that don't mutate the vector and return tuple
    def get_add_tuple(self, other, integer=False):
        x = self.x + other[0]
        y = self.y + other[1]
        if integer:
            return int(round(x)), int(round(y))
        return x, y

    def get_sub_tuple(self, other, integer=False):
        x = self.x - other[0]
        y = self.y - other[1]
        if integer:
            return int(round(x)), int(round(y))
        return x, y

    def get_mult_tuple(self, scalar, integer=False):
        x = self.x * scalar
        y = self.y * scalar
        if integer:
            return int(round(x)), int(round(y))
        return x, y

    def get_div_tuple(self, scalar, integer=False):
        x = self.x / scalar
        y = self.y / scalar
        if integer:
            return int(round(x)), int(round(y))
        return x, y

    # operator overloads
    def __add__(self, other):
        return self.get_add_tuple(other)

    def __sub__(self, other):
        return self.get_sub_tuple(other)

    def __mul__(self, other):
        return self.get_mult_tuple(other)

    def __div__(self, other):
        return self.get_div_tuple(other)
