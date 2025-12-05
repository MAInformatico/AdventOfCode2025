import sys
import re as regex

def part_1(batteries):
    total = 0

    for battery in batteries:

        current = battery if isinstance(battery, str) else battery[0]
        current = current.strip()
        n = len(current)
        if n < 2:
            continue

        best = -1

        for i in range(n - 1):
            tens = int(current[i])
            ones = max(int(ch) for ch in current[i+1:])
            value = tens * 10 + ones
            if value > best:
                best = value

        if best >= 0:
            total += best

    return total



def part_2(batteries):

    def max_subsequence_of_length(s: str, k: int) -> str:
        stack = []
        to_remove = len(s) - k
        for i in s:
            while stack and to_remove > 0 and stack[-1] < i:
                stack.pop()
                to_remove -= 1
            stack.append(i)
        # If we didn't remove enough, trim the end
        return ''.join(stack[:k])

    total = 0
    k = 12
    for battery in batteries:
        current = battery if isinstance(battery, str) else battery[0]
        current = current.strip()
        n = len(current)
        if n < k:
            continue

        best_value = max_subsequence_of_length(current, k)
        total += int(best_value)

    return total


def day_1(filename, first=True):
    batteries = []

    with open(filename) as file:
        for line in file:
            row = line.strip()
            batteries.append(row)
    
    if first:
        return part_1(batteries)
    
    return part_2(batteries)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day3 part 1: {day_1(arg, True)}')
        print(f'day3 part 2: {day_1(arg, False)}')