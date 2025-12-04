exemple = "data/exemples/day4.txt"

path_data = "data/day4.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [line for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    L = {}
    for i in range(len(input[0])):
        for j in range(len(input)):
            if input[i][j] == '.':
                continue

            L[(i, j)] = []
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (k == 0 and l == 0) or (i + k < 0) or (j + l < 0) or (i + k >= len(input[0])) or (j + l >= len(input)):
                        continue
                    L[(i, j)].append(input[i + k][j + l])

    return sum(1 if L[k].count('@') < 4 else 0 for k in L.keys())

def solve_part2(path: str) -> int:
    input = parse(path)

    count = 0
    removed = True

    while removed:
        removed = False
        L = {}

        for i in range(len(input[0])):
            for j in range(len(input)):
                if input[i][j] == '.':
                    continue

                L[(i, j)] = []
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (k == 0 and l == 0) or (i + k < 0) or (j + l < 0) or (i + k >= len(input[0])) or (j + l >= len(input)):
                            continue
                        L[(i, j)].append(input[i + k][j + l])

        for (i, j) in L.keys():
            if L[(i, j)].count('@') < 4:
                removed = True
                count += 1
                input[i] = input[i][:j] + '.' + input[i][j + 1:]

    return count

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 13

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 43

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
