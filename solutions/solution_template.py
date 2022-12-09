def solve1(lines):
    pass

def solve2(lines):
    pass


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_simple_lines))
    print(solve2(input_simple_lines))

