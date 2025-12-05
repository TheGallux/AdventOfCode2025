exemple = "data/exemples/day5.txt"

path_data = "data/day5.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L1 = []
    L2 = []
    switch = True
    for line in L:
        if (line == ''):
            switch = False
            continue

        if switch:
            l, r = line.split('-')
            L1.append((int(l), int(r)))

        else:
            L2.append(int(line))

    return L1, L2

def solve_part1(path: str) -> int:
    input = parse(path)
    ranges, values = input

    counter = 0
    for val in values:
        for (l, r) in ranges:
            if val >= l and val <= r:
                counter += 1
                break

    return counter

def solve_part2(path: str) -> int: # 320924701371383 is too low
    input = parse(path)
    ranges, _ = input

    # removed l2, r2 when it exists l1, r1 such as
    # --|-----|-----|----|---
    #  l1    l2    r2   l1
    to_delete = []
    for i in range(len(ranges)):
        l, r = ranges[i]
        for j in range(len(ranges)):
            if i == j:
                continue
            l2, r2 = ranges[j]
            if (l >= l2) and (r <= r2):
                to_delete.append(i)
                break

    for i in to_delete[::-1]:
        ranges.pop(i)

    """ old_merge
    changed = -1
    while changed != 0:
        changed = 0
        for i in range(len(ranges)):
            l1, r1 = ranges[i]
            for j in range(i + 1, len(ranges)):
                l2, r2 = ranges[j]
                if (l1 < l2) and (r1 < r2) and (l2 < r1):
                    ranges[j] = (r1 + 1, r2)
                    changed += 1
                if (l1 > l2) and (r1 > r2) and (l1 < r2):
                    ranges[i] = (r2 + 1, r1)
                    changed += 1
    """
    # TODO: implement this https://preview.redd.it/2025-day-5-a-fast-algorithm-v0-3uwsqtohjc5g1.gif?width=600&auto=webp&s=fe3bb46f7c10b1970504b22d105c98144c93201c
    ranges.sort(key=lambda couple: couple[0])
    for i in range(1, len(ranges)):
        i = len(ranges) - i - 1
        l1, r1 = ranges[i]
        l2, r2 = ranges[i - 1]

    counter = 0
    for l, r in ranges:
        counter += r - l + 1

    return counter

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 3

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 14

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
