class Generator:
    def __init__(self, seed, factor, criteria_multiple):
        self.current = seed
        self.factor = factor
        self.criteria_multiple = criteria_multiple

    def __next__(self):
        self.current = (self.current * self.factor) % 2147483647
        while self.current % self.criteria_multiple != 0:
            self.current = (self.current * self.factor) % 2147483647
        return self.current


power = 2 ** 16


def leftmost_bits(n):
    return n % power

generator_a = Generator(634, 16807, 4)
generator_b = Generator(301, 48271, 8)
print('--Gen. A--  --Gen. B--')
for i in range(0, 5):
    print('{a: >10} {b: >10}'.format(a=generator_a.__next__(),
                                     b=generator_b.__next__()))
matches_count = 0
for i in range(0, int(5e6)):
    if leftmost_bits(generator_a.__next__()) == \
            leftmost_bits(generator_b.__next__()):
        matches_count += 1
print(matches_count)
