exemple = "data/exemples/dayN.txt"

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

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == None

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == None

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
