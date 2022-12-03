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

def play(opp_shape, own_shape):
    if (own_shape + 1) % 3 == opp_shape:
        # lost
        return own_shape + 1
    elif (opp_shape + 1) % 3 == own_shape:
        # won
        return own_shape + 7
    else:
        # draw
        return own_shape + 4

with open("input.txt", "r") as f:
    sum = 0
    for round in f:
        opp_shape = round[0]
        own_shape = round[2]
        sum += play(opp_shapes[opp_shape], own_shapes[own_shape])
    print(sum)
