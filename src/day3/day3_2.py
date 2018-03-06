import numpy

def eval_size(max_num):
    i = 0
    while (2 * i + 1) ** 2 < max_num:
        i += 1
    return i


def eval_size2(max_num):
    side = 1
    cur_num = 25
    while (cur_num < max_num):
        cur_num *= 16
        side += 1
    return side


print(eval_size2(347991 * 4) + 1)

matrix = numpy.zeros((13, 13), numpy.dtype('i'))
matrix[6][6] = 4
print(matrix)