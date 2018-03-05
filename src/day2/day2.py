import sys


def read_lines():
    return [[int(num) for num in line.split('\t')] for
            line in sys.stdin.readlines()]


def max_min_checksum(line):
    return max(line) - min(line)


def divisors_checksum(line):
    last_i = len(line)
    for i in range(0, last_i):
        i_item = line[i]
        for j in range(0, last_i):
            j_item = line[j]
            if i != j and i_item % j_item == 0:
                return i_item // j_item


def compute_checksum(f):
    lines = read_lines()
    checksum_list = [f(line) for line in lines]
    return sum(checksum_list)


print(compute_checksum(max_min_checksum))
print(compute_checksum(divisors_checksum))
