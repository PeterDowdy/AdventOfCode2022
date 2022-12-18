data = []
with open("day18.txt") as f:
    data = [x.strip() for x in f.readlines()]


cubes = set()

for c in data:
    x, y, z = [int(x) for x in c.split(",")]
    cubes.add((x, y, z))


def get_neighbors(c):
    x, y, z = c
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if abs(dx) + abs(dy) + abs(dz) == 1:
                    neighbors.append((x + dx, y + dy, z + dz))
    return neighbors


total_sides = 0

for c in cubes:
    total_sides += 6 - len([x for x in get_neighbors(c) if x in cubes])

print(total_sides)
