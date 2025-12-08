exemple = "data/exemples/day8.txt"

path_data = "data/day8.txt"

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
        return True

def parse(path: str) -> list[str]:
    L = []

    with open(path, 'r') as file:
        for line in file:
            L.append(line.strip())

    L = [list(map(int, line.split(','))) for line in L]

    return L

def solve_part1(path: str) -> int:
    input = parse(path)
    n = len(input)
    tours = 10 if n == 20 else 1000

    edges = []
    for i in range(n):
        x1, y1, z1 = input[i]
        for j in range(i + 1, n):
            x2, y2, z2 = input[j]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((d, i, j))

    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)
    for d, i, j in edges[:tours]:
        dsu.union(i, j)

    components = {}
    for i in range(n):
        p = dsu.find(i)
        components[p] = components.get(p, 0) + 1

    biggest = sorted(components.values())[-3:]
    return biggest[0] * biggest[1] * biggest[2]

def solve_part2(path: str) -> int:
    input = parse(path)
    n = len(input)

    edges = []
    for i in range(n):
        x1, y1, z1 = input[i]
        for j in range(i + 1, n):
            x2, y2, z2 = input[j]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((d, i, j))

    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)

    for d, i, j in edges:
        if dsu.union(i, j):
            if sum(1 for x in range(n) if dsu.find(x) == x) == 1:
                return input[i][0] * input[j][0]

value_ex1 = solve_part1(exemple)
print("Exemple Part 1:", value_ex1)
assert value_ex1 == 40

value_ex2 = solve_part2(exemple)
print("Exemple Part 2:", value_ex2)
assert value_ex2 == 25272

print()
print()

print("PART 1:", solve_part1(path_data))
print("-------")
print()
print("PART 2:", solve_part2(path_data))
print("-------")
