

with open("day3-input.txt") as f:
    lines = f.readlines()


def solve(right, down):
    count = 0

    j = 0

    for i in range(0, len(lines), down):
        if lines[i][j] == '\n':
            lines.remove(lines[i][j])
        if lines[i][j] == '#':
            # print(i, j)
            count += 1

        j += right
        if j >= 31:
            j -= 31
    return count


if __name__ == '__main__':
    part1 = solve(3, 1)
    part2 = solve(3, 1) * solve(1, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2)
    print(part1)
    print(part2)


