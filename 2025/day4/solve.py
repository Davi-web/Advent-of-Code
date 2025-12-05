with open("2025\day4\input.txt") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]

def part1():
    m = len(grid)
    n = len(grid[0])
    print(f"Grid size: {m} rows, {n} columns")
    accessible_by_forklift = 0
    # check number of adjacent cells with @ for each @ cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                count = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '@':
                        count += 1
                print(f"Cell ({i}, {j}) has {count} adjacent @ cells.")
                if count < 4:
                    accessible_by_forklift += 1
    print(f"Total accessible @ cells: {accessible_by_forklift}")

def part2():
    m = len(grid)
    n = len(grid[0])
    print(f"Grid size: {m} rows, {n} columns")
    total_removed = 0
    iteration = 1

    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while True:
        to_remove = []

        # 1. Scan full grid to find removable cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    count = 0
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '@':
                            count += 1
                    if count < 4:
                        to_remove.append((i, j))

        print(f"Iteration {iteration}: found {len(to_remove)} removable cells")

        # 2. If nothing to remove → stop
        if not to_remove:
            break

        # 3. Remove all at once
        for i, j in to_remove:
            grid[i][j] = '.'

        total_removed += len(to_remove)
        iteration += 1

    print("Total removed:", total_removed)
    return total_removed
if __name__ == '__main__':
    # print(grid)
    part2()