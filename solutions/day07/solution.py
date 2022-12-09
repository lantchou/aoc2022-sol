class DirTree():
    
    def __init__(self, name, parent, size, leaf):
        self.children = None if leaf else []
        self.name = name
        self.parent = parent
        self.size = size

    def print_tree(self, level=0):
        tabs = "\t" * level
        print(f"{tabs}{self.name} ({self.size})")
        if self.children is not None:
            for child in self.children:
                child.print_tree(level + 1)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def calc_dir_tree(lines):
    root = DirTree("/", None, 0, False)
    curr_dir = root
    i = 0
    while i < len(lines):
        cmd = lines[i].split()
        if cmd[1] == "ls":
            # ls
            i += 1
            children = []
            while i < len(lines) and not lines[i].startswith("$"):
                if lines[i].startswith("dir"):
                    _, name = lines[i].split()
                    children.append(DirTree(name, curr_dir, 0, False))
                else:
                    size, name = lines[i].split()
                    children.append(DirTree(name, curr_dir, int(size), True))
                i += 1
            curr_dir.children = children
        else:
            # cd
            next_dir_name = cmd[2]
            if next_dir_name == "..":
                curr_dir = curr_dir.parent
            elif next_dir_name == "/":
                curr_dir = root
            else:
                curr_dir = next(child for child in curr_dir.children
                                if child.name == next_dir_name)
            i += 1
    return root


def calc_small_dirs_total_size(dir_tree):
    if dir_tree.children is None:
        return 0

    size_sum = 0
    if dir_tree.size <= 100000:
        size_sum += dir_tree.size

    if dir_tree.children is not None:
        size_sum += sum(calc_small_dirs_total_size(child)
                        for child in dir_tree.children)

    return size_sum


def calc_dir_sizes(dir_tree):
    if dir_tree.children is None:
        return dir_tree.size

    size_sum = 0
    for child in dir_tree.children:
        size_sum += calc_dir_sizes(child)

    dir_tree.size = size_sum
    return size_sum


def list_dirs(dir_tree):
    if dir_tree.children is None:
        return []

    dirs = [dir_tree]
    for child in dir_tree.children:
        for child_dir in list_dirs(child):
            dirs.append(child_dir)

    return dirs


def solve1(lines: list[str]):
    dir_tree = calc_dir_tree(lines)
    calc_dir_sizes(dir_tree) 
    return calc_small_dirs_total_size(dir_tree)


def solve2(lines):
    dir_tree = calc_dir_tree(lines)
    calc_dir_sizes(dir_tree) 
    free_space = 70000000 - dir_tree.size
    dirs = list_dirs(dir_tree)
    min_dir_size = dir_tree.size
    for dir in dirs:
        if free_space + dir.size >= 30000000 and dir.size < min_dir_size:
            min_dir_size = dir.size
    return min_dir_size
    

if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

