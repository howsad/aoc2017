def read_data():
    return input()


def to_digits(char_seq):
    return [int(c) for c in char_seq]


def one_digit_offset(seq): return 1


def half_seq_offset(seq): return len(seq) // 2


def solve_captcha(char_seq, offset):
    num_seq = to_digits(char_seq)
    matched = [i[1] for i in enumerate(num_seq) if
               i[1] == num_seq[(i[0] + offset(char_seq)) % len(num_seq)]]
    return sum(matched)


def solve(offset):
    data = read_data()
    digits = to_digits(data)
    captcha = solve_captcha(digits, offset)
    print(captcha)