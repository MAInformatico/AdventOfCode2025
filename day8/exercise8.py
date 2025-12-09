import sys
import heapq
import math
import dsu


def part_1(j_boxes):    
    heap = []
    circuit = {}

    for i in range(len(j_boxes)):
        for j in range(i+1, len(j_boxes)):
            ax, ay, az = j_boxes[i]
            bx, by, bz = j_boxes[j]
            dist = math.dist((int(ax), int(ay), int(az)), (int(bx), int(by), int(bz)))
            heapq.heappush(heap, (dist, i, j))
    
    dsu_obj = dsu.DSU(len(j_boxes))

    top_1000 = heapq.nsmallest(1000, heap)
    for _, i, j in top_1000:
        dsu_obj.union(i, j)

    circuit = {}
    for i in range(len(j_boxes)):
        r = dsu_obj.find(i)
        circuit[r] = circuit.get(r, 0) + 1

    sizes = sorted(circuit.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part_2(j_boxes):
    heap = []

    for i in range(len(j_boxes)):
        for j in range(i+1, len(j_boxes)):
            ax, ay, az = map(int, j_boxes[i])
            bx, by, bz = map(int, j_boxes[j])
            dist = math.dist((ax, ay, az), (bx, by, bz))
            heapq.heappush(heap, (dist, i, j))
    
    dsu_obj = dsu.DSU(len(j_boxes))
    sorted_pairs = heapq.nsmallest(len(heap), heap)
    num_sets = len(j_boxes)

    for _, i, j in sorted_pairs:
        if dsu_obj.union(i, j):
            num_sets -= 1
            if num_sets == 1:
                return int(j_boxes[i][0]) * int(j_boxes[j][0])

def day_8(filename, first=True):
    j_boxes = []

    with open(filename) as file:
        for line in file:
            row = line.strip().split(",")            
            j_boxes.append(row)

    if first:
        return part_1(j_boxes)
    
    return part_2(j_boxes)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day8 part 1: {day_8(arg, True)}')
        print(f'day8 part 2: {day_8(arg, False)}')