import sys
import re as regex

def part_1(products):
    result = 0
    regexpression = r'^([1-9][0-9]*)\1$'
    pattern = regex.compile(regexpression)

    for i in range(len(products[0])):        
        first, second = products[0][i].split('-')
        #checking the intervals values
        for j in range(int(first), int(second)+1):
            match = pattern.match(str(j))
            if match:
                result += j
    return result



def part_2(products):
    result = 0
    regexpression = r'^([1-9][0-9]*)(\1)+$' #This is the difference with part 1
    pattern = regex.compile(regexpression)

    for i in range(len(products[0])):        
        first, second = products[0][i].split('-')
        #checking the intervals values
        for j in range(int(first), int(second)+1):
            match = pattern.match(str(j))
            if match:
                result += j
    return result


def day_1(filename, first=True):
    products = []

    with open(filename) as file:
        for line in file:
            row = line.strip().split(",")            
            products.append((row))               

    if first:
        return part_1(products)
    
    return part_2(products)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day2 part 1: {day_1(arg, True)}')
        print(f'day2 part 2: {day_1(arg, False)}')