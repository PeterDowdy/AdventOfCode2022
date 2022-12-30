data = []
with open("day17.txt") as f:
    data = [x.strip() for x in f.readlines()][0]

stop_at = 10000


def next_piece():
    ctr = 0
    pieces = [
        [[0, 0, 1, 1, 1, 1, 0]],
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
        ],
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
        ],
    ]
    while True:
        yield [x for x in pieces[ctr]]
        ctr += 1
        if ctr == len(pieces):
            ctr = 0


def next_gust():
    ctr = 0
    while True:
        yield data[ctr]
        ctr += 1
        if ctr == len(data):
            ctr = 0


map = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def print_map():
    print()
    for line in map:
        print("".join(["#" if x == 2 else "@" if x == 1 else "." for x in line]))


rock_gen = next_piece()
gust_gen = next_gust()
active_rock = None
rock_count = 0
ctr = 0
rock_size = 0
while True:
    ctr += 1
    gust = next(gust_gen)
    if not active_rock:
        rock_size = 0
        if rock_count == stop_at:
            break
        active_rock = next(rock_gen)
        rock_count += 1
        for r in active_rock:
            rock_size += sum(r)
        if len(map) != 3:
            for n in range(0, len(map)):
                if any(map[n]):
                    break
            map = map[n - 3 :]
        for row in active_rock[::-1]:
            map = [[x for x in row]] + map
    adds = []
    removes = []
    collision = False
    if gust == ">":
        for y in range(0, len(map)):
            if map[y][-1] == 1:
                collision = True
            for x in range(0, 6):
                if map[y][x] == 1:
                    if map[y][x + 1] == 2:
                        collision = True
                    adds.append((x + 1, y))
                    removes.append((x, y))
            if len(adds) == rock_size:
                break

    elif gust == "<":
        for y in range(0, len(map)):
            if map[y][0] == 1:
                collision = True
            for x in range(1, 7):
                if map[y][x] == 1:
                    if map[y][x - 1] == 2:
                        collision = True
                    adds.append((x - 1, y))
                    removes.append((x, y))
            if len(adds) == rock_size:
                break
    if not collision:
        for x, y in removes:
            map[y][x] = 0
        for x, y in adds:
            map[y][x] = 1
    should_stop = any([x == 1 for x in map[-1]])
    check_count = 0
    for y in range(0, len(map)):
        for x in range(0, 7):
            if map[y][x] == 1:
                check_count += 1
            if map[y][x] == 1 and map[y + 1][x] == 2:
                should_stop = True
                break
        if check_count == rock_size:
            break
        if should_stop:
            break
    if should_stop:
        freeze_count = 0
        for y in range(0, len(map)):
            for x in range(0, 7):
                if map[y][x] == 1:
                    freeze_count += 1
                    map[y][x] = 2
            if freeze_count == rock_size:
                break
        active_rock = None
        continue
    adds = []
    removes = []
    for y in range(0, len(map)):
        for x in range(0, 7):
            if map[y][x] == 1:
                adds.append((x, y + 1))
                removes.append((x, y))
        if len(adds) == rock_size:
            break

    for x, y in removes:
        map[y][x] = 0
    for x, y in adds:
        map[y][x] = 1


for n in range(0, len(map)):
    if any(map[n]):
        break

print(f"The tower is {len(map)-n} blocks high.")
