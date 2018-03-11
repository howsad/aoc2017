from day10.day10_commons import *
import itertools
import functools


def read_lengths_from_string(s):
    return [ord(c) for c in s] + [17, 31, 73, 47, 23]


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
        return functools.reduce(lambda x, y: x * 256 + y, dense_hash)


def hash_from_string(s):
    lst = init_lst()
    computer = KnotHashComputer()
    return computer.compute_hash(lst, read_lengths_from_string(s))
