def char_list():
    return [chr(i) for i in range(ord('a'), ord('a') + 16)]


def spin(x):
    def spin_(lst):
        return lst[-x:] + lst[: -x]
    return spin_


def exchange(a, b):
    def exchange_(lst):
        nlst = lst[:]
        nlst[a], nlst[b] = nlst[b], nlst[a]
        return nlst
    return exchange_


def partner(a, b):
    def partner_(lst):
        i = lst.index(a)
        j = lst.index(b)
        nlst = lst[:]
        nlst[i], nlst[j] = nlst[j], nlst[i]
        return nlst
    return partner_


def read_instructions():
    def read_instruction(instruction_def):
        if instruction_def[0] == 's':
            return spin(int(instruction_def[1:]))
        else:
            a, b = instruction_def[1:].split('/')
            if instruction_def[0] == 'x':
                return exchange(int(a), int(b))
            elif instruction_def[0] == 'p':
                return partner(a, b)
    return [read_instruction(idef) for idef in input().split(',')]


def apply_instructions(lst, instructions):
    for instruction in instructions:
        lst = instruction(lst)
    return lst


def find_period(instructions_):
    start = char_list()
    memo = [start]
    lst_ = apply_instructions(char_list(), instructions_)
    while start != lst_:
        memo.append(lst_)
        lst_ = apply_instructions(lst_, instructions_)
    return memo


instructions = read_instructions()
lst = char_list()

end_position = apply_instructions(lst, instructions)
print(end_position)

period = find_period(instructions)
index = int(1e9) % len(period)
print(index)
for perm in enumerate(period):
    print("{} {}".format(perm[0], perm[1]))
print(''.join(period[index]))
