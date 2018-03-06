def sign(val):
    if val == 0:
        return 0
    return val / abs(val)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def normalize(self):
        return Vector(sign(self.x), sign(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def is_zero(self):
        return self.x == 0 and self.y == 0

    def one_less(self):
        return self.__add__(self.normalize() * -1)

    def __str__(self):
        return "X = %d, Y = %d" % (self.x, self.y)

