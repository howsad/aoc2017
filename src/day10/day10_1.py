from day10.day10_commons import *


def read_lengths():
    return [int(x) for x in input().strip().split(',')]


class KnotHashComputer:
    def __init__(self):
        self.knot_tier = KnotTier()

    def compute_hash(self, lst, lengths):
        self.knot_tier.tie_knots(lst, lengths)
        return lst[0] * lst[1]

l = init_lst()
lengths = read_lengths()
hash_computer = KnotHashComputer()
hash_computer.compute_hash(l, lengths)

print(l)
print("hash = %d" % (l[0] * l[1]))
