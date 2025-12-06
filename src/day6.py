exemple = "data/exemples/day6.txt"

path_data = "data/day6.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [[n for n in line.split(" ") if n != ''] for line in L[:-1]] + [[o for o in L[-1].split(" ") if o != '']]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    ##return sum(eval(input[-1][i].join([input[j][i] for j in range(len(input[i]) - 1)])) for i in range(len(input)))
    L = ['' for _ in range(len(input[0]))]

    for j in range(len(input[0])):
        for i in range(len(input) - 1):
            L[j] += input[i][j] + input[-1][j]

    return sum(eval(column[:-1]) for column in L)


def parse2(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [line for line in L[:-1]] + [[o for o in L[-1].split(" ") if o != '']]

    return L

def solve_part2(path: str) -> int:
    input = parse2(path)

    print(input)

    return None

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 4277556

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 3263827

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
