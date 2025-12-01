exemple = "data/exemples/day1.txt"

path_data = "data/day1.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [(line[0], int(line[1:])) for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    counter = 0
    dial = 50

    for rotation in input:
        direction = -1 if rotation[0] == 'L' else 1

        dial = (direction * rotation[1] + dial + 100) % 100
        if (dial == 0):
            counter += 1

    return counter

def solve_part2(path: str) -> int:
    input = parse(path)

    counter = 0
    dial = 50

    for rotation in input:
        start = dial
        direction = -1 if rotation[0] == 'L' else 1
        end = (dial + direction * rotation[1]) % 100

        if (direction == 1):
            base = (100 - start) % 100
        else:
            base = start

        if (base == 0):
            base = 100

        if (base <= rotation[1]):
            counter += 1 + (rotation[1] - base) // 100

        dial = end

    return counter

print("Exemple Part 1:", solve_part1(exemple))
print("Exemple Part 2:", solve_part2(exemple))

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
