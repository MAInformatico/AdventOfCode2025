import sys
import re

def part_1(problems, ops):
    total = 0

    for numbers, op in zip(problems, ops):
        if op == '+':
            local = sum(numbers)
        elif op == '*':
            local = 1
            for n in numbers:
                local *= n
        total += local

    return total


def part_2(problems):
    pass


def day_6(filename, first=True):
    problems = []
    ops = []

    with open(filename) as file:
        lines = [line.rstrip('\n') for line in file]

    ops_line = lines[-1]
    ops = [c for c in ops_line if c in '+*']

    num_problems = len(ops)
    problems = [[] for _ in range(num_problems)]

    for line in lines[:-1]:
        matches = list(re.finditer(r'\d+', line))
        for i, m in enumerate(matches):
            problems[i].append(int(m.group()))

    if first:
        return part_1(problems, ops)
    
    return part_2(problems)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day6 part 1: {day_6(arg, True)}')
        print(f'day6 part 2: {day_6(arg, False)}')