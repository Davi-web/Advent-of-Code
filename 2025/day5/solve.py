with open("input.txt") as f:
    # input is range of numbers a new line seperator and then integers on new lines
    lines = f.readlines()
    ranges = []
    fresh = []
    for line in lines:
        if '-' in line:
            a, b = line.strip().split('-')
            ranges.append((int(a), int(b)))
        elif line.strip().isdigit():
            fresh.append(int(line.strip()))
        
    print(ranges)
    print(fresh)

def merge(intervals):
    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or merged[-1][1] < s:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged

def in_range(x, intervals):
    # binary search for the interval whose start <= x
    l, r = 0, len(intervals)-1
    while l <= r:
        mid = (l+r)//2
        s, e = intervals[mid]
        if s <= x <= e:
            return True
        if x < s:
            r = mid-1
        else:
            l = mid+1
    return False
def part1(fresh_id_ranges, fresh_ids):
    merged_ranges = merge(sorted(fresh_id_ranges))
    return sum(in_range(x, merged_ranges) for x in fresh_ids)
def part2(fresh_id_ranges):
    merged_ranges = merge(sorted(fresh_id_ranges))
    total_covered = 0
    for s, e in merged_ranges:
        total_covered += (e - s + 1)
    return total_covered
if __name__ == "__main__":
    res = part1(ranges, fresh)
    print(f"Part 1: {res}")
    res2 = part2(ranges)
    print(f"Part 2: {res2}")