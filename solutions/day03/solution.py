CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR_TO_PRIO = {char: i + 1 for i, char in enumerate(CHARS)}


def solve1(lines):
    score_sum = 0
    for line in lines:
        mid = len(line) // 2
        first_half_chars = set(line[0:mid])
        second_half_chars = set(line[mid:])
        common_char = (first_half_chars & second_half_chars).pop()
        score_sum += CHAR_TO_PRIO[common_char]
    return score_sum


def solve2(lines):
    score_sum = 0
    for i in range(0, len(lines), 3):
        part1chars = set(lines[i])   
        part2chars = set(lines[i + 1])   
        part3chars = set(lines[i + 2])   
        common_char = (part1chars & part2chars & part3chars).pop()
        score_sum += CHAR_TO_PRIO[common_char]
    return score_sum


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

