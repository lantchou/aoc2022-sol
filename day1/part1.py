if __name__ == "__main__":
    with open("input.txt", "r") as f:
        curr_sum = 0
        max_sum = 0
        for line in f:
            line = line.strip()
            if line == "":
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0
            else:
                curr_sum += int(line)

        print(max(max_sum, curr_sum))
