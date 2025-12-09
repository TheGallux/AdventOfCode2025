exemple = "data/exemples/day9.txt"

path_data = "data/day9.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L2 = []
    for i in range(len(L)):
        x, y = L[i].split(',')
        L2.append((int(x), int(y)))

    return L2

def solve_part1(path: str) -> int:
    input = parse(path)

    biggest_area = -1
    for i in range(len(input)):
        x1, y1 = input[i]
        for j in range(i + 1, len(input)):
            x2, y2 = input[j]

            size_rect = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            biggest_area = max(biggest_area, size_rect)

    return biggest_area

def parse2(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L2 = []
    for i in range(len(L)):
        x, y = L[i].split(',')
        L2.append((int(x), int(y)))



    return map

def solve_part2(path: str) -> int:
    input = parse2(path)


    return None

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 50

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
#assert value_ex2 == 24

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
