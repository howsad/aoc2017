from day19.pipe import *


def read_input():
    import sys
    return [line[:-1] for line in sys.stdin.readlines()]


def find_entrance(grid):
    return grid[0].index('|'), 0


def is_inbounds(cell, grid):
    x = cell[0]
    y = cell[1]
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def get_char(cell, grid):
    return grid[cell[1]][cell[0]]


def turn(pipe, cell, grid):
    direction = pipe.direction
    for next_dir in possible_turns[direction]:
        next_cell = next_dir.next_cell(cell)
        if is_inbounds(next_cell, grid) and get_char(next_cell, grid) != ' ':
            print(next_dir.name)
            return Pipe(next_dir)

grid = read_input()
cur_cell = find_entrance(grid)
cur_pipe = Pipe(d)
pipes = [cur_pipe]
cell = cur_pipe.next_cell(cur_cell)
move_count = 1
while True:
    char = get_char(cell, grid)
    if char == '+':
        next_pipe = turn(cur_pipe, cell, grid)
        cur_pipe = next_pipe
        pipes.append(cur_pipe)
    if char.isalpha():
        cur_pipe.label = char
    if char == ' ':
        break
    cur_cell = cell
    cell = cur_pipe.next_cell(cur_cell)
    move_count += 1

labels = ''.join([pipe.label for pipe in pipes if pipe.label is not None])
print(labels)
print(move_count)
