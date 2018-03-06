from day4.day4_commons import all_unique, count_valid_passphrases


def is_valid(phrase):
    return all_unique(phrase)


valid_passphrases_count = count_valid_passphrases(is_valid)
print(valid_passphrases_count)
