exemple_part1 = "data/exemples/dayN_part1.txt"
exemple__part1 = "data/exemples/dayN_part2.txt"

path_data = "data/dayN.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [line for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    return None

def solve_part2(path: str) -> int:
    input = parse(path)

    return None

print("Exemple Part 1:", solve_part1(exemple_part1))
print("Exemple Part 2:", solve_part2(exemple_part2))

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
