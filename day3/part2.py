from part1 import CHAR_TO_PRIO


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        score_sum = 0
        lines = f.read().splitlines()
        for i in range(0, len(lines), 3):
            part1chars = set(lines[i])   
            part2chars = set(lines[i + 1])   
            part3chars = set(lines[i + 2])   
            common_char = (part1chars & part2chars & part3chars).pop()
            score_sum += CHAR_TO_PRIO[common_char]
        print(score_sum)
