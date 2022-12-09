def solve1(pairs):
    contain_count = 0
    for pair in pairs:
        lo1, hi1, lo2, hi2 = parse_pair(pair)
        if lo1 <= lo2 <= hi2 <= hi1 or lo2 <= lo1 <= hi1 <= hi2:
            contain_count += 1
    return contain_count


def solve2(pairs):
    overlap_count = 0
    for pair in pairs:
        lo1, hi1, lo2, hi2 = parse_pair(pair)
        if max(lo1, lo2) < min(hi1, hi2) + 1:
            overlap_count += 1
    return overlap_count


def parse_pair(pair: str):
    range1, range2 = pair.split(",")
    lo1, hi1 = range1.split("-")
    lo2, hi2 = range2.split("-")
    return int(lo1), int(hi1), int(lo2), int(hi2)


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

