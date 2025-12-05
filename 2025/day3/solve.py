with open("2025\day3\input.txt") as f:
    battery_banks = f.readlines()

def part1(battery_banks: list[str]):
    res = 0
    for battery_bank in battery_banks:
        battery_bank = battery_bank.strip()
        print(f"Processing battery bank: {battery_bank}")
        n = len(battery_bank)
        max_num = -1
        for i in range(n):
            for j in range(i + 1, n):
                temp = int(battery_bank[i] + battery_bank[j])
                max_num = max(max_num, temp)

        res += max_num
    print(f"Total sum of max charge levels: {res}")


def part2(battery_banks: list[str]):
    res = 0
    k = 12

    for battery_bank in battery_banks:
        s = battery_bank.strip()

        stack = []
        to_remove = len(s) - k  # how many characters we can drop

        for c in s:
            while stack and to_remove > 0 and stack[-1] < c:
                stack.pop()
                to_remove -= 1
            stack.append(c)

        # take only first k characters (in case not enough removals were used)
        best = ''.join(stack[:k])

        res += int(best)
    print(f"Total sum of best charge levels: {res}")
    return res
      

if __name__ == '__main__':
    # part1(battery_banks)
    part2(battery_banks)

    
