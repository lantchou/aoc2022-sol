CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR_TO_PRIO = {char: i + 1 for i, char in enumerate(CHARS)}


def get_priority(rucksack: str):
    mid = len(rucksack) // 2
    first_half_chars = set(rucksack[0:mid])
    second_half_chars = set(rucksack[mid:])
    common_char = (first_half_chars & second_half_chars).pop()
    return CHAR_TO_PRIO[common_char]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        score_sum = 0
        for line in f:
            score_sum += get_priority(line.strip()) 
        print(score_sum)
