buffer = [0]
curr_pos = 0
steps = 337
current_after_0 = None
for i in range(1, 50000001):
    curr_pos += steps
    curr_pos %= i
    buffer.insert(curr_pos + 1, i)
    if curr_pos == 0:
        current_after_0 = i
        print("Current value after 0 is {}".format(current_after_0))
    curr_pos += 1
print(buffer)
print("The one that goes after 2017 is {}". format(buffer[buffer.index(2017) + 1]))
