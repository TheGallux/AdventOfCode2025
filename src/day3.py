exemple = "data/exemples/day3.txt"

path_data = "data/day3.txt"

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [[int(c) for c in line] for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    S = 0

    for line in input:
        index_max = line.index(max(line[:-1]))
        second_max = line.index(max(line[index_max + 1:]))

        S += 10 * line[index_max] + line[second_max]

    return S

def solve_part2(path: str) -> int:
    input = parse(path)

    def biggest_substring(arr):
        pile = []
        i = len(arr) - 12

        for c in arr:
            while pile != [] and c > pile[-1] and i > 0:
                pile.pop()
                i -= 1
            pile.append(c)

        pile = pile[:12]

        return sum([10**i * pile[11 - i] for i in range(len(pile))])

    S = 0
    for line in input:
        S += biggest_substring(line)

    return S

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 357

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 3121910778619

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
