from day4.day4_commons import all_unique, count_valid_passphrases
from collections import Counter


def freeze_dict(d):
    return tuple((k, d[k]) for k in sorted(d.keys()))


def is_valid(phrase):
    letters_in_words_count = [freeze_dict(Counter(word)) for word in phrase]
    return all_unique(letters_in_words_count)


valid_passphrases_count = count_valid_passphrases(is_valid)
print(valid_passphrases_count)
