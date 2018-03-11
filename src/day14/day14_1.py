import day10.day10_2_hash as day10
from collections import Counter


def print_grid(grid):
    for row in grid:
        print(row)

grid = []
key = 'vbqugkhl'
grid_size = 128
for i in range(0, grid_size):
    grid.append(
        format(
            day10.hash_from_string(key + '-' + str(i)),
            "0%db" % grid_size)
    )

print_grid(grid)
occupied_count = sum([Counter(row)['1'] for row in grid])
print("Occupied count = %d" % occupied_count)


def to_mutable(grid):
    return [list(row) for row in grid]


def to_immutable(grid):
    return [''.join(row).replace('0', ' ') for row in grid]


def flood_fill(grid, start, char):
    start_y = start[1]
    start_x = start[0]
    if grid[start_y][start_x] != '1':
        return False
    grid[start_y][start_x] = char
    if start_x > 0:
        flood_fill(grid, (start_x - 1, start_y), char)
    if start_y > 0:
        flood_fill(grid, (start_x, start_y - 1), char)
    if start_x < grid_size - 1:
        flood_fill(grid, (start_x + 1, start_y), char)
    if start_y < grid_size - 1:
        flood_fill(grid, (start_x, start_y + 1), char)
    return True

grid_divided = to_mutable(grid)
fill_char_ord = ord('1') + 1
regions_count = 0
for start_y in range(0, grid_size):
    for start_x in range(0, grid_size):
        is_new_region = flood_fill(
            grid_divided,
            (start_x, start_y),
            chr(fill_char_ord)
        )
        if is_new_region:
            regions_count += 1
            fill_char_ord += 1
print_grid(to_immutable(grid_divided))
print("Regions count = %d" % regions_count)
