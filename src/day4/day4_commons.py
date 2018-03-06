import sys
from collections import Counter


def read_phrases():
    return [line.strip().split(' ') for line in sys.stdin.readlines()]


def all_unique(elems):
    return Counter(elems).most_common(1)[0][1] == 1


def count_valid_passphrases(validation_f):
    phrases = read_phrases()
    return len([1 for phrase in phrases if validation_f(phrase)])

