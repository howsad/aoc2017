from day3.vector import Vector


class Direction:
    def __init__(self, vector):
        self.vector = vector

    def set_next(self, next_dir):
        self.next = next_dir

    def mult(self, amplitude):
        vector = self.vector
        return vector[0] * amplitude, vector[1] * amplitude


r = Direction(Vector(1, 0))
u = Direction(Vector(0, 1))
l = Direction(Vector(-1, 0))
d = Direction(Vector(0, -1))

r.set_next(u)
u.set_next(l)
l.set_next(d)
d.set_next(r)

directions = [r, u, l, d]


def to_direction(vector):
    normalized = vector.normalize()
    for direction in directions:
        if direction.vector == normalized:
            return direction
