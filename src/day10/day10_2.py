from day10.day10_commons import *
import itertools
import functools


def read_lengths():
    return [ord(c) for c in input().strip()] + [17, 31, 73, 47, 23]


class KnotHashComputer:
    def __init__(self):
        self.knot_tier = KnotTier()

    def compute_hash(self, lst, lengths):
        for i in range(0, 64):
            self.knot_tier.tie_knots(lst, lengths)
        groups = itertools.groupby(enumerate(lst), lambda x: x[0] // 16)
        sparse_hash = [[x[1] for x in group[1]] for group in groups]
        dense_hash = [functools.reduce(lambda x, y: x ^ y, h)
                      for h in sparse_hash]
        return ''.join(['%02x' % n for n in dense_hash])


lengths = read_lengths()
lst = init_lst()
computer = KnotHashComputer()
knot_hash = list(computer.compute_hash(lst, lengths))
print(''.join(knot_hash))
