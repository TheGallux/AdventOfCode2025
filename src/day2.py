exemple = "data/exemples/day2.txt"

path_data = "data/day2.txt"

def parse(path: str) -> list[str]:

    with open(path, 'r') as file:
        for line in file:
            L = line.strip().split(',')

    L = [line.split('-') for line in L]
    L = [(int(line[0]), int(line[1])) for line in L]

    return L

def solve_part1(path: str) -> int:
    def is_invalid_id(nb: int) -> bool:
        # return True if nb = xyzxyz
        nombre = str(nb)
        indice_milieu = len(nombre) // 2
        return (nombre[:indice_milieu] == nombre[indice_milieu:])

    input = parse(path)

    counter = 0

    for start, end in input:
        while start != end + 1:

            if (is_invalid_id(start)):
                counter += start

            start += 1

    return counter

def solve_part2(path: str) -> int:
    def is_invalid_id(nb: int) -> bool:
        nb = str(nb)

        string = ""
        for c in nb:
            string += c
            if (len(string) > len(nb) / 2):
                return False

            if (len(nb) % len(string) == 0):
                string2 = string * (len(nb) // len(string))
                if string2 == nb:
                    return True

        return False # shouln't happen


    input = parse(path)

    counter = 0

    for start, end in input:
        while start != end + 1:

            if (is_invalid_id(start)):
                counter += start

            start += 1

    return counter

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 1227775554

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 4174379265

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
