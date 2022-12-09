def parse_stacks(lines):
    stack_bottom = 0
    while not lines[stack_bottom][1].isnumeric():
        stack_bottom += 1

    stacks = []
    width = len(lines[0])
    for col in range(1, width, 4):
        stack = []
        row = stack_bottom - 1
        while row >= 0 and lines[row][col].isalpha():
            stack.append(lines[row][col])
            row -= 1
        stacks.append(stack)

    return stacks, stack_bottom


def parse_step(step):
    _, move_count, _, from_crate, _, to_crate = step.split(" ")
    return int(move_count), int(from_crate) - 1, int(to_crate) - 1


def get_message(stacks):
    msg = []
    for stack in stacks:
        msg.append(stack[-1])
    return "".join(msg)


def solve1(lines: list[str]):
    stacks, stack_bottom = parse_stacks(lines)
    
    # perform steps
    for i in range(stack_bottom + 2, len(lines)):
        move_count, from_crate, to_crate = parse_step(lines[i])

        # move top move_count crates from from_crate to to_crate
        for _ in range(move_count):
            stacks[to_crate].append(stacks[from_crate].pop())
        
    return get_message(stacks)


def solve2(lines: list[str]):
    stacks, stack_bottom = parse_stacks(lines)
    
    # perform steps
    for i in range(stack_bottom + 2, len(lines)):
        move_count, from_crate, to_crate = parse_step(lines[i])

        # move top move_count crates from from_crate to to_crate in reverse order
        moved_crates = [stacks[from_crate].pop() for _ in range(move_count)]
        stacks[to_crate] += reversed(moved_crates)
        
    # get message from stacks
    return get_message(stacks)


if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))


