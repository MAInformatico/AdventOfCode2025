import sys
import re
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger

def solve_machine_pulp(target, buttons, num_counters):
    num_buttons = len(buttons)

    A = [[0]*num_buttons for _ in range(num_counters)]
    for i in range(num_counters):
        for j, b in enumerate(buttons):
            if i in b:
                A[i][j] = 1

    prob = LpProblem("ButtonPresses", LpMinimize)

    x = [LpVariable(f"x{j}", lowBound=0, cat=LpInteger) for j in range(num_buttons)]

    for i in range(num_counters):
        prob += lpSum(A[i][j] * x[j] for j in range(num_buttons)) == target[i]

    prob += lpSum(x)

    prob.solve()

    total_presses = sum(int(v.varValue) for v in x)
    return total_presses


def solve_machine_linear(target, buttons, num_lights):
    B = len(buttons)
    rows = []
    for light in range(num_lights):
        mask = 0
        for j, btn in enumerate(buttons):
            if (btn >> light) & 1:
                mask |= (1 << j)
        rhs = (target >> light) & 1
        rows.append([mask, rhs])

    pivot_col = {}
    row = 0
    for col in range(B):
        pivot = None
        for r in range(row, num_lights):
            if (rows[r][0] >> col) & 1:
                pivot = r
                break
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        pivot_col[col] = row
        for r in range(num_lights):
            if r != row and ((rows[r][0] >> col) & 1):
                rows[r][0] ^= rows[row][0]
                rows[r][1] ^= rows[row][1]
        row += 1

    for mask, rhs in rows:
        if mask == 0 and rhs == 1:
            return None

    x0 = 0
    for col, r in pivot_col.items():
        if rows[r][1]:
            x0 |= (1 << col)

    free_vars = [c for c in range(B) if c not in pivot_col]
    null_vectors = []
    for free in free_vars:
        v = 1 << free
        for col, r in pivot_col.items():
            if (rows[r][0] >> free) & 1:
                v |= (1 << col)
        null_vectors.append(v)

    best = None
    k = len(null_vectors)
    for mask in range(1 << k):
        x = x0
        for i in range(k):
            if (mask >> i) & 1:
                x ^= null_vectors[i]
        presses = x.bit_count()
        if best is None or presses < best:
            best = presses

    return best

def part_1(machines):
    total_presses = 0
    for line in machines:
        # parsing target diagram
        diagram = re.search(r"\[([.#]+)\]", line).group(1)
        target = 0
        for i, c in enumerate(diagram):
            if c == '#':
                target |= (1 << i)

        # parsing buttons
        buttons_raw = re.findall(r"\(([\d,]+)\)", line)
        button_masks = []
        for b in buttons_raw:
            indices = list(map(int, b.split(',')))
            mask = 0
            for idx in indices:
                mask |= (1 << idx)
            button_masks.append(mask)

        # using linear algebra to solve
        presses = solve_machine_linear(target, button_masks, len(diagram))
        total_presses += presses

    return total_presses


def part_2(machines):
    total_presses = 0
    for line in machines:
        buttons_raw = re.findall(r"\(([\d,]+)\)", line)
        button_masks = [list(map(int, b.split(','))) for b in buttons_raw]

        target_raw = re.search(r"\{([\d,]+)\}", line).group(1)
        target = list(map(int, target_raw.split(',')))

        # Resolver con pulp
        presses = solve_machine_pulp(target, button_masks, len(target))
        total_presses += presses

    return total_presses


def day_10(filename, first=True):
    machines = []
    with open(filename) as file:
        for line in file:
            row = line.strip("\n")
            machines.append(row)
    
    
    if first:
        return part_1(machines)

    return part_2(machines)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day10 part 1: {day_10(arg, True)}')
        print(f'day10 part 2: {day_10(arg, False)}')