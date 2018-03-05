from day1.day1_functions import *

test_data = [
    {
        'chars': '1122',
        'nums': [1, 1, 2, 2],
        'captcha': 3,
    }, {
        'chars': '1111',
        'captcha': 4,
    }, {
        'chars': '1234',
        'captcha': 0,
    }, {
        'chars': '91212129',
        'captcha': 9,
    },
]

test_data_2 = [
    {
        'chars': '1212',
        'captcha': 6,
    }, {
        'chars': '1221',
        'captcha': 0,
    }, {
        'chars': '123425',
        'captcha': 4,
    }, {
        'chars': '123123',
        'captcha': 12,
    }, {
        'chars': '12131415',
        'captcha': 4,
    },
]

chars0 = test_data[0]['chars']
digits = to_digits(chars0)
if digits != test_data[0]['nums']:
    raise Exception("Incorrect to digits")
else:
    print("Correct to digits conversion")


def test_captcha(test_data_, offset):
    for test_entry in test_data_:
        chars_ = test_entry['chars']
        captcha = solve_captcha(chars_, offset)
        if captcha != test_entry['captcha']:
            raise Exception(
                "Incorrect captcha for %s, actual = %s" % (
                    chars_, captcha)
            )
        else:
            print("Correct captcha %s" % chars_)


test_captcha(test_data, one_digit_offset)
test_captcha(test_data_2, half_seq_offset)
