from day3.direction import *
import numpy


class SpiralIterator:
    def __init__(self, coords):
        self.coords = coords
        self.sidelen = 1
        self.side_left = 1
        self.direction = r

    def turn(self):
        next_dir = self.direction.next
        next_length = self.sidelen
        if next_dir == r or next_dir == l:
            next_length += 1
        self.direction = next_dir
        self.sidelen = next_length
        self.side_left = next_length

    def next(self):
        coords = self.coords
        if self.side_left == 0:
            self.turn()
        self.coords += self.direction.vector
        self.side_left -= 1
        return coords


def read_int():
    return int(input())


def next_(current_number, iterator):
    return current_number + 1, iterator.next()


def sum_neighbors(matrix, x, y):
    neighbors = matrix[y - 1][x - 1: x + 2] + matrix[y][x - 1: x + 2] + \
                matrix[y + 1][x - 1: x + 2]
    print("neighbors of %d, %d are %s" % (x, y, neighbors))
    return sum(
        neighbors
    )


def next__(matrix, x, y):
    next_val = sum_neighbors(matrix, x, y)
    matrix[y][x] = next_val
    return next_val

destination_number = read_int()

number, iterator = 1, SpiralIterator(Vector(6, 6))
iterator.next()

# for i in range(0, destination_number):
#     number, coords = next_(number, iterator)
#
# print("Distance is %d" % coords.manhattan_distance())

matrix = numpy.zeros((13, 13), numpy.dtype('i'))
matrix[6, 6] = 1
while number <= destination_number:
    print(matrix)
    coords = iterator.next()
    print(coords)
    number = next__(matrix, coords.x, coords.y)

print(matrix)
print(number)