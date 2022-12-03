opp_shapes = {
    "A": 0,
    "B": 1,
    "C": 2 
}

def play(opp_shape, choice):
    if choice == "X":
        # you need to lose
        return (opp_shape - 1) % 3 + 1
    elif choice == "Z":
        # you need to win
        return (opp_shape + 1) % 3 + 7
    else:
        # you need to draw
        return opp_shape + 4

with open("input.txt", "r") as f:
    sum = 0
    for round in f:
        opp_shape = round[0]
        choice = round[2]
        sum += play(opp_shapes[opp_shape], choice)
    print(sum)
