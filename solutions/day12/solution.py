import sys
from collections import deque


def solve1(lines):

    # find starting pos "S"
    start_row = 0
    while (start_col := lines[start_row].find("S")) == -1:
        start_row += 1

    # find destination pos "E"
    dest_row = 0
    while (dest_col := lines[dest_row].find("E")) == -1:
        dest_row += 1

    grid = [[c for c in line] for line in lines]
    grid[start_row][start_col] = "a"
    grid[dest_row][dest_col] = "z"

    return find_shortest_path(grid, start_row, start_col, dest_row, dest_col)


def solve2(lines):
    # find "S" position
    start_row = 0
    while (start_col := lines[start_row].find("S")) == -1:
        start_row += 1

    # find destination pos "E"
    dest_row = 0
    while (dest_col := lines[dest_row].find("E")) == -1:
        dest_row += 1

    grid = [[c for c in line] for line in lines]
    grid[start_row][start_col] = "a"
    grid[dest_row][dest_col] = "z"

    # find shortest path from all positions at elevation "a"
    min_dist = sys.maxsize
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "a":
                min_dist = min(min_dist, find_shortest_path(
                    grid, row, col, dest_row, dest_col))

    return min_dist


def find_shortest_path(grid, start_row, start_col, dest_row, dest_col):
    height = len(grid)
    width = len(grid[0])

    dist = {(r, c): sys.maxsize for r in range(height) for c in range(width)}
    dist[(start_row, start_col)] = 0
    visited = set([(start_row, start_col)])
    queue = deque([(start_row, start_col)])
    while queue:
        row, col = queue.popleft()

        if (row, col) == (dest_row, dest_col):
            break

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_row = row + dy
            next_col = col + dx
            if 0 <= next_row < height and \
               0 <= next_col < width and \
               can_step(grid[row][col], grid[next_row][next_col]) and \
               (next_row, next_col) not in visited:

                temp_dist = dist[(row, col)] + 1
                if temp_dist < dist[(next_row, next_col)]:
                    dist[(next_row, next_col)] = temp_dist

                visited.add((next_row, next_col))
                queue.append((next_row, next_col))

    return dist[(dest_row, dest_col)]


def can_step(h1, h2):
    return ord(h2) - ord(h1) <= 1


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))
