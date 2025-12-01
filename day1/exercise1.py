import sys


def part_1(sequences):
    count = 0
    current_value = 50
    for sequence in sequences:
        if sequence[0] == "L":
            current_value -= int(sequence[1:])
        elif sequence[0] == "R":
            current_value += int(sequence[1:])
        current_value %= 100
        if current_value == 0:
            count += 1
    return count        



def part_2(sequences):
    # Count every click that causes the dial to point at 0 (including during a rotation)
    count = 0
    current_value = 50
    for sequence in sequences:
        direction = sequence[0]
        distance = int(sequence[1:])
        if direction == "R":
            needed_k = (100 - (current_value % 100)) % 100
        else:
            needed_k = current_value % 100
        if needed_k == 0:
            needed_k = 100

        if distance >= needed_k:
            count += 1 + (distance - needed_k) // 100

        if direction == "R":
            current_value = (current_value + distance) % 100
        else:
            current_value = (current_value - distance) % 100

    return count


def day_1(filename, first=True):
    sequences = []

    with open(filename) as file:
        for line in file:
            row = line.strip()            
            sequences.append((row))       

    if first:
        return part_1(sequences)
    
    return part_2(sequences)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day1 part 1: {day_1(arg, True)}')
        print(f'day1 part 2: {day_1(arg, False)}')