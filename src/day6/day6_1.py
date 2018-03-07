def read_input():
    return [int(n) for n in input().strip().split('\t')]


def find_max(banks):
    max_blocks = max(banks)
    for i in range(0, len(banks)):
        if max_blocks == banks[i]:
            return i


def realloc(banks):
    i = find_max(banks)
    blocks_left = banks[i]
    banks[i] = 0
    banks_count = len(banks)
    all_get_blocks_count = blocks_left // banks_count
    leftovers = blocks_left % banks_count
    for j in range(i + 1, i + 1 + banks_count):
        j_wrapped = j % banks_count
        if leftovers > 0:
            banks[j_wrapped] += all_get_blocks_count + 1
            leftovers -= 1
        else:
            banks[j_wrapped] += all_get_blocks_count


inp = read_input()
prev_states_set = set()
prev_states_list = []
cycles_count = 0
while True:
    t = tuple(inp)
    if prev_states_set.__contains__(t):
        break
    else:
        cycles_count += 1
        prev_states_set.add(t)
        prev_states_list.append(t)
        realloc(inp)

cycle_length = len(prev_states_list) - prev_states_list.index(tuple(inp))
print("Cycles count = %d. Cycle length = %d" %(cycles_count, cycle_length))
