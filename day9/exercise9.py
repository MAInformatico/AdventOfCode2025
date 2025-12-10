import sys

def part_1(points):
    
    points = [tuple(map(int, point.split(','))) for point in points]
    red_tiles = points 
    max_area = 0

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area

def part_2(points):
    pass

def day_9(filename, first=True):
    points = []
    with open(filename) as file:
        for line in file:
            row = line.strip()
            points.append(row)
    
    if first:
        return part_1(points)

    return part_2(points)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day9 part 1: {day_9(arg, True)}')
        print(f'day9 part 2: {day_9(arg, False)}')