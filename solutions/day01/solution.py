def solve1(lines):
    curr_sum = 0
    max_sum = 0
    for line in lines:
        if line == "":
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    return max(max_sum, curr_sum)


def solve2(lines):
    sums = []
    curr_sum = 0
    for line in lines:
        line = line.strip()
        if line == "":
            sums.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    sums.append(curr_sum)
    sums.sort(reverse=True)
    return sums[0] + sums[1] + sums[2]


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

