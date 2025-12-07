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

def solve_part2(path: str) -> int:
    ranges, _ = parse(path)

    ranges.sort(key=lambda x: x[0])
    merged = []
    for l, r in ranges:
        if not merged:
            merged.append((l, r))
        else:
            last_l, last_r = merged[-1]
            if l <= last_r + 1:
                merged[-1] = (last_l, max(last_r, r))
            else:
                merged.append((l, r))

    return sum(r - l + 1 for l, r in merged)

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
