from collections import deque


def find_marker(datastream, n):
    last_n = deque()
    i = 0
    while i < len(datastream) and len(set(last_n)) < n:
        last_n.append(datastream[i])
        if len(last_n) == n + 1:
            last_n.popleft()
        i += 1
    return i


def solve1(lines):
    datastream = lines[0]
    return find_marker(datastream, 4)


def solve2(lines):
    datastream = lines[0]
    return find_marker(datastream, 14)


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

