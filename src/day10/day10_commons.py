def init_lst():
    return [i for i in range(0, 256)]


class KnotTier:
    def __init__(self):
        self.pos = 0
        self.skip = 0

    def tie_a_knot(self, start, length, lst):
        if length < 2:
            return
        end = (start + length - 1) % len(lst)
        lst[start], lst[end] = lst[end], lst[start]
        if length == 2:
            return
        start += 1
        start %= len(lst)
        self.tie_a_knot(start, length - 2, lst)

    def tie_knots(self, lst, lengths):
        for length in lengths:
            self.tie_a_knot(self.pos, length, lst)
            self.pos += length + self.skip
            self.pos %= len(lst)
            self.skip += 1
