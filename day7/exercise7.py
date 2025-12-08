import sys
import re

def part_1(hazes_grid):
    grid = [list(row[0]) if isinstance(row[0], str) else row for row in hazes_grid]

    rows = len(grid)
    cols = len(grid[0])
    
    # S position searching
    start_row, start_col = None, None
    for r, row in enumerate(grid):
        if 'S' in row:
            start_row = r
            start_col = row.index('S')
            break
    if start_row is None:
        raise ValueError("S value not founded at the map")
    
    # active 
    active_beams = {(start_row, start_col)}
    splits = 0
    
    # while there are active beams
    while active_beams:
        next_beams = set()
        for r, c in active_beams:
            # if we are at the bottom, stop
            if r + 1 >= rows:
                continue
            cell_below = grid[r + 1][c]
            if cell_below == '.':
                next_beams.add((r + 1, c))
            elif cell_below == '^':
                # each beam splits into two
                splits += 1
                # two new beams are created
                if c - 1 >= 0:
                    next_beams.add((r + 1, c - 1))
                if c + 1 < cols:
                    next_beams.add((r + 1, c + 1))
        active_beams = next_beams
    
    return splits



def part_2(grid):
    grid = [list(row[0]) if isinstance(row[0], str) else row for row in grid]

    rows = len(grid)
    cols = len(grid[0])

    # S position searching
    start_row, start_col = None, None
    for r, row in enumerate(grid):
        if 'S' in row:
            start_row = r
            start_col = row.index('S')
            break
    if start_row is None:
        raise ValueError("No se encuentra S en el mapa")

    # memoizacion dictionary: key = (row, col), value = timelines number from that position
    memo = {}

    def count_from(r, c):
        if (r, c) in memo:
            return memo[(r, c)]

        if r >= rows - 1:
            memo[(r, c)] = 1
            return 1

        cell_below = grid[r + 1][c]

        if cell_below == '.':
            total = count_from(r + 1, c)
        elif cell_below == '^':
            total = 0
            if c - 1 >= 0:
                total += count_from(r + 1, c - 1)
            if c + 1 < cols:
                total += count_from(r + 1, c + 1)
        else:
            total = count_from(r + 1, c)

        memo[(r, c)] = total
        return total

    return count_from(start_row, start_col)
    


def day_7(filename, first=True):
    grid = []

    with open(filename) as file:
        for line in file:
            row = line.strip().split(" ")
            grid.append(row)

    if first:
        return part_1(grid)
    
    return part_2(grid)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day7 part 1: {day_7(arg, True)}')
        print(f'day7 part 2: {day_7(arg, False)}')