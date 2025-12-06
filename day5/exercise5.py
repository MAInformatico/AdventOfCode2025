import sys
import bisect

def part_1(ranges):

    blank_index = ranges.index("")
    range_lines = ranges[:blank_index]
    id_lines = ranges[blank_index + 1:]

    intervals = []
    for line in range_lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            intervals.append((start, end))

    intervals.sort()
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    
    starts = [s for s, e in merged]
    ends = [e for s, e in merged]

    fresh = 0
    for i in id_lines:
        value = int(i)
        idx = bisect.bisect_right(starts, value)
        if idx == 0:
            continue
        if ends[idx - 1] >= value:
            fresh += 1

    return fresh    

def part_2(ranges):
    blank_index = ranges.index("")
    range_lines = ranges[:blank_index]
    
    intervals = []
    
    for line in range_lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            intervals.append((start, end))
    
    intervals.sort()
    
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    fresh = 0
    for start, end in merged:
        fresh += end - start + 1 
    
    return fresh


def day_1(filename, first=True):
    ranges = []

    with open(filename) as file:
        for line in file:
            row = line.strip()
            ranges.append(row)
    
    if first:
        return part_1(ranges)
    
    return part_2(ranges)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day5 part 1: {day_1(arg, True)}')
        print(f'day5 part 2: {day_1(arg, False)}')