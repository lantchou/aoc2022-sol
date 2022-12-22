import math


class Monkey:

    def __init__(self, items, op, op_val, test_div, monkey_if_true,
                 monkey_if_false):
        self.items = items
        self.op = op
        self.op_val = op_val
        self.test_div = test_div
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.inspect_count = 0

    def throw(self, item):
        self.items.append(item)

    def do_round(self, monkeys, div_by_three, cm=None):
        for item in self.items:
            val = item if self.op_val == "old" else int(self.op_val)
            item = item * val if self.op == "*" else item + val
            if div_by_three:
                item //= 3            
            item %= cm  # to avoid dealing with big numbers
            if item % self.test_div == 0:
                monkeys[self.monkey_if_true].throw(item)
            else:
                monkeys[self.monkey_if_false].throw(item)
            self.inspect_count += 1

        self.items = []


def parse_monkeys(lines):
    monkeys = []
    i = 0
    for i in range(0, len(lines), 7):
        items = [int(item) for item in
                 "".join(lines[i + 1].strip().split()[2:]).split(",")] 
        op_words = lines[i + 2].split()
        op = op_words[-2]
        op_val = op_words[-1]
        test_div = int(lines[i + 3].split()[-1])
        monkey_if_true = int(lines[i + 4].split()[-1]) 
        monkey_if_false = int(lines[i + 5].split()[-1]) 
        monkeys.append(Monkey(items, op, op_val, test_div, monkey_if_true,
                              monkey_if_false))
    return monkeys


def calc_monkey_business(monkeys):
    sorted_monkeys = sorted(monkeys, key=lambda m: -m.inspect_count)
    return sorted_monkeys[0].inspect_count * sorted_monkeys[1].inspect_count


def calc_monkeys_lcm(monkeys):
    lcm = 1
    for monkey in monkeys:
        lcm = lcm * monkey.test_div // math.gcd(lcm, monkey.test_div)
    return lcm


def solve1(lines):
    monkeys = parse_monkeys(lines)
    
    for _ in range(20):
        for monkey in monkeys:
            monkey.do_round(monkeys, True, calc_monkeys_lcm(monkeys))

    return calc_monkey_business(monkeys)
        
def solve2(lines): 
    monkeys = parse_monkeys(lines)

    for _ in range(10000):
        for monkey in monkeys:
            monkey.do_round(monkeys, False, calc_monkeys_lcm(monkeys))

    return calc_monkey_business(monkeys)

if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

