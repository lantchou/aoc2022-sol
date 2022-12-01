if __name__ == "__main__":
    with open("input.txt", "r") as f:
        sums = []
        curr_sum = 0
        for line in f:
            line = line.strip()
            if line == "":
                sums.append(curr_sum)
                curr_sum = 0
            else:
                curr_sum += int(line)

        sums.append(curr_sum)
        sums.sort(reverse=True)
        print(sums[0] + sums[1] + sums[2])
