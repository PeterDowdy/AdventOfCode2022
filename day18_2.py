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


min_x = min([x[0] for x in cubes])
max_x = max([x[0] for x in cubes])
min_y = min([x[1] for x in cubes])
max_y = max([x[1] for x in cubes])
min_z = min([x[2] for x in cubes])
max_z = max([x[2] for x in cubes])

potential_air_pockets = set()

for z in range(min_z - 1, max_z + 2):
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y, z) not in cubes:
                potential_air_pockets.add((x, y, z))

known_good = set()
known_bad = set()


def can_reach_air(c):
    closed_pockets = set()
    open_pockets = set([c])
    while True:
        next_open_pockets = set()
        if any(x in known_bad for x in closed_pockets) or any(
            x in known_bad for x in open_pockets
        ):
            known_bad.update(closed_pockets)
            known_bad.update(open_pockets)
            return False
        if any(x in known_good for x in closed_pockets) or any(
            x in known_good for x in open_pockets
        ):
            known_good.update(closed_pockets)
            known_good.update(open_pockets)
            return True

        for c_ in open_pockets:
            if (
                c_[0] < min_x
                or c_[1] < min_y
                or c_[2] < min_z
                or c_[0] > max_x
                or c_[1] > max_y
                or c_[2] > max_z
            ):
                known_bad.update(closed_pockets)
                known_bad.update(next_open_pockets)
                return False
            for n in get_neighbors(c_):
                if n not in cubes and n not in closed_pockets and n not in open_pockets:
                    next_open_pockets.add(n)
            closed_pockets.add(c_)
        if not len(open_pockets):
            known_good.update(closed_pockets)
            known_good.update(next_open_pockets)
            return True
        open_pockets = next_open_pockets


real_air_pockets = [x for x in potential_air_pockets if can_reach_air(x)]

total_sides = 0

for c in cubes:
    total_sides += 6 - len(
        [x for x in get_neighbors(c) if x in cubes or x in real_air_pockets]
    )
print(total_sides)
