opp_shapes = {
    "A": 0,
    "B": 1,
    "C": 2 
}

own_shapes = {
    "X": 0,
    "Y": 1,
    "Z": 2
}


def solve1(lines):
    score_sum = 0
    for round in lines:
        opp_shape = opp_shapes[round[0]]
        own_shape = own_shapes[round[2]]
        if (own_shape + 1) % 3 == opp_shape:
            # lost
            score = own_shape + 1
        elif (opp_shape + 1) % 3 == own_shape:
            # won
            score = own_shape + 7
        else:
            # draw
            score = own_shape + 4
        score_sum += score
    return score_sum


def solve2(lines):
    score_sum = 0
    for round in lines:
        opp_shape = opp_shapes[round[0]]
        choice = round[2]
        if choice == "X":
            # you need to lose
            score = (opp_shape - 1) % 3 + 1
        elif choice == "Z":
            # you need to win
            score = (opp_shape + 1) % 3 + 7
        else:
            # you need to draw
            score = opp_shape + 4
        score_sum += score

    return score_sum


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

