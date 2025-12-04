import math
with open("input.txt") as f:
    lines = f.readlines()
    turns = []
    for line in lines:
        turns += line.split()
def part1():
    arrow = 50
    res = 0
    for turn in turns:
        direction = turn[0]
        value = int(turn[1:])
        if direction == 'L':
            arrow = (arrow - value) % 100
        elif direction == 'R':
            arrow = (arrow + value) % 100
        if arrow == 0:
            res += 1
    print(arrow)
    print(res)
import math

def part2():
    pos = 50
    hits = 0

    for t in turns:
        direction = t[0]
        steps = int(t[1:])

        delta = steps if direction == "R" else -steps
        start = pos
        end = (start + delta) % 100

        # full loops always count
        hits += abs(delta) // 100

        # partial movement
        leftover = abs(delta) % 100

        if delta > 0:  # moving right
            dist_to_zero = (100 - start) % 100
            if dist_to_zero > 0 and leftover >= dist_to_zero:
                hits += 1

        else:  # moving left
            dist_to_zero = start % 100
            if dist_to_zero > 0 and leftover >= dist_to_zero:
                hits += 1

        pos = end

    return hits




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Part 1:", end=" ")
    part1()
    print("Part 2:", end=" ")
    print(part2())
