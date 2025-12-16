import sys

def dfs(node,graph,memo):
    if node == "out":
        return 1
    if node in memo:
        return memo[node]

    memo[node] = sum(dfs(neighbor,graph,memo) for neighbor in graph[node])
    return memo[node]

def dfs_2(node, seen_dac, seen_fft, graph, memo):
    if node == "out":
        return 1 if seen_dac and seen_fft else 0

    key = (node, seen_dac, seen_fft)
    if key in memo:
        return memo[key]

    total = 0
    for neighbor in graph[node]:
        total += dfs_2(
            neighbor,
            seen_dac or neighbor == "dac",
            seen_fft or neighbor == "fft",
            graph,
            memo
        )

    memo[key] = total
    return total



def part_1(graph):
    memo = {}
    return dfs("you", graph, memo)


def part_2(graph):
    memo = {}
    return dfs_2("svr", False, False, graph, memo)


def day_11(filename, first=True):
    graph = {}

    with open(filename) as file:
        for line in file:
            src, dests = line.strip().split(":")
            graph[src] = dests.strip().split()

    graph.setdefault("out", [])

    if first:
        return part_1(graph)
    return part_2(graph)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day11 part 1: {day_11(arg, True)}')
        print(f'day11 part 2: {day_11(arg, False)}')