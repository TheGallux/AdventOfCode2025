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

    def biggest_substring(L):
        big = []

        return sum([10**i * big[len(L) - 1 - i] for i in range(len(big))])

    S = 0

    exp = ["987654321111", "811111111119", "434234234278", "434234234278"]
    for line in input:
        print("===", ''.join(list(map(str,line))))
        s = biggest_substring(line)
        print("   ", exp[0])
        exp = exp[1:]
        print("   ",s)
        S += s

    #print(biggest_substring([3, 4, 2, 2, 4, 4, 5, 3, 3, 6, 2, 3, 5, 8, 4, 2, 7, 4, 7, 2, 2, 6, 6, 2, 3, 9, 7, 9, 4, 5, 1, 2, 8, 4, 6, 4, 4, 7, 8, 8, 5, 9, 3, 5, 5, 6, 2, 3, 4, 5, 6, 3, 4, 8, 3, 7, 5, 5, 4, 5, 8, 5, 6, 3, 4, 7, 7, 8, 7, 7, 5, 8, 5, 6, 9, 2, 7, 7, 4, 5, 1, 9, 4, 8, 7, 7, 7, 5, 5, 5, 3, 8, 2, 4, 5, 9, 1, 7, 4, 5]))

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
