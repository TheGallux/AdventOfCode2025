exemple = "data/exemples/day7.txt"

path_data = "data/day7.txt"
import time
def insert(queue, cpl):
    queue.append(cpl)

def pop(q):
    m = 0
    for i in range(len(q)):
        if q[i][1] < q[m][1]:
            m = i
    val = q[m]
    del q[m]
    return val

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [[c for c in line] for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)

    counter = 0
    priority_queue = [(input[0].index('S'), 1)]
    while priority_queue != []:
        index, hauteur = pop(priority_queue)

        if (hauteur >= len(input)):
            continue

        if (input[hauteur][index] == '|' or input[hauteur][index] == '.'):
            input[hauteur][index] = '|'
            insert(priority_queue, (index, hauteur + 1))

        elif (input[hauteur][index] == '&'):
            continue

        else: #ie we have a splitter which has not been met yet
            counter += 1
            input[hauteur][index] = '&'
            if (index - 1) > 0:
                input[hauteur][index - 1] = '|'
                insert(priority_queue, (index - 1, hauteur))
            if (index + 1) < len(input[0]):
                input[hauteur][index + 1] = '|'
                insert(priority_queue, (index + 1, hauteur))

    return counter

def solve_part2(path: str) -> int:
    input = parse(path)

    dico = {}
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '^':
                dico[(i, j)] = -1

    def count_size(i, j):
        if i >= len(input):
            return 1

        if input[i][j] == '.':
            return count_size(i + 1, j)

        else:
            if dico[(i, j)] != -1:
                return dico[(i, j)]

            dico[(i, j)] = 0
            if (j - 1) >= 0:
                dico[(i, j)] = count_size(i + 1, j - 1)
            if (j + 1) < len(input[0]):
                dico[(i, j)] += count_size(i + 1, j + 1)
            return dico[(i, j)]

    return count_size(1, input[0].index('S'))

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 21

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 40

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
