import functools
import itertools


def read_input():
    return input().split(',')


def to_vector(s):
    return {
        'n': (0, 2),
        'ne': (1, 1),
        'se': (1, -1),
        's': (0, -2),
        'sw': (-1, -1),
        'nw': (-1, 1),
    }[s]


def total_steps(vector):
    hor_transits = abs(vector[0])
    vert_transits = (abs(vector[1]) - hor_transits) // 2
    return hor_transits + vert_transits


inp = read_input()
vectors = [to_vector(s) for s in inp]
accumulate = itertools.accumulate(
    vectors,
    lambda x, y: (x[0] + y[0], x[1] + y[1])
)
max_steps = max(accumulate, key=total_steps)
print('Max steps = %s, total steps = %d' % (max_steps, total_steps(max_steps)))
