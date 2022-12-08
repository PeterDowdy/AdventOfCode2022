data = []
with open("day8.txt") as f:
    data = [x.strip() for x in f.readlines()]


grid = {}
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        grid[(x, y)] = int(data[y][x])

invisible = set()

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        this_cell = grid[(x, y)]
        west = max([v for k, v in grid.items() if k[0] < x and k[1] == y])
        east = max([v for k, v in grid.items() if k[0] > x and k[1] == y])
        north = max([v for k, v in grid.items() if k[0] == x and k[1] < y])
        south = max([v for k, v in grid.items() if k[0] == x and k[1] > y])
        if all([h >= this_cell for h in [west, east, north, south]]):
            invisible.add((x, y))

print(len(list(grid.keys())) - len(invisible))
