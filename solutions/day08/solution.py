def solve1(lines):
    width = len(lines)
    vis_count = width ** 2 - (width - 2) ** 2
    for row in range(1, width - 1):
        for col in range(1, width - 1):
            h = int(lines[row][col])
            if all(int(lines[row][col - i]) < h for i in range(1, col + 1)) or \
               all(int(lines[row][col + i]) < h for i in range(1, width - col)) or \
               all(int(lines[row - i][col]) < h for i in range(1, row + 1)) or \
               all(int(lines[row + i][col]) < h for i in range(1, width - row)):
                vis_count += 1

    return vis_count


def solve2(lines):
    w = len(lines)
    max_scenic_score = 0
    for r in range(1, w - 1):
        for c in range(1, w - 1):
            h = int(lines[r][c])
            scenic_score = \
                calc_view_dist(int(lines[r][c - i]) < h for i in range(1, c + 1)) * \
                calc_view_dist(int(lines[r][c + i]) < h for i in range(1, w - c)) * \
                calc_view_dist(int(lines[r - i][c]) < h for i in range(1, r + 1)) * \
                calc_view_dist(int(lines[r + i][c]) < h for i in range(1, w - r))
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


def calc_view_dist(vis_list):
    vd = 0
    for vis in vis_list:
        vd += 1
        if not vis:
            break
    return vd
                

if __name__ == "__main__":
    with open("input_simple.txt", "r") as f:
        input_simple_lines = f.read().splitlines()

    with open("input.txt", "r") as f:
        input_lines = f.read().splitlines()

    print(solve1(input_lines))
    print(solve2(input_lines))

