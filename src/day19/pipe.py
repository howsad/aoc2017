class Direction:
    def __init__(self, name, dx, dy):
        self.name = name
        self.dx = dx
        self.dy = dy

    def next_cell(self, cell):
        return cell[0] + self.dx, cell[1] + self.dy


class Pipe:
    def __init__(self, direction):
        self.direction = direction
        self.label = None

    def next_cell(self, cell):
        return self.direction.next_cell(cell)

d = Direction('d', 0, 1)
u = Direction('u', 0, -1)
l = Direction('l', -1, 0)
r = Direction('r', 1, 0)

possible_turns = {
    d: [l, r],
    u: [l, r],
    l: [u, d],
    r: [u, d],
}