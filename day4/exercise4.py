import sys
import papergrid

def part_1(paper_map):
    grid = papergrid.PaperGrid(paper_map)
    return grid.count_accessible()



def part_2(paper_map):
    grid = papergrid.PaperGrid(paper_map)
    removed = 0
    while True:
        to_remove = []
        for r in range(grid.rows):
            for c in range(grid.cols):
                if grid.is_accessible(r, c):
                    to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid.remove_paper(r, c)
            removed += 1
    return removed


def day_4(filename, first=True):
    paper_map = []

    with open(filename) as file:
        for line in file:
            row = line.strip()
            paper_map.append(row)
    
    if first:
        return part_1(paper_map)
    
    return part_2(paper_map)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day4 part 1: {day_4(arg, True)}')
        print(f'day4 part 2: {day_4(arg, False)}')