import os

data = []
with open("day14.txt") as f:
    data = [x.strip() for x in f.readlines()]

grid = {}

for line in data:
    instructions = line.split(" -> ")
    steps = []
    for i in instructions:
        x, y = i.split(",")
        x = int(x)
        y = int(y)
        steps.append((x, y))
    for n in range(0, len(steps) - 1):
        step_1 = steps[n]
        step_2 = steps[n + 1]
        if step_1[0] > step_2[0]:
            while step_1[0] >= step_2[0]:
                grid[step_1] = "#"
                step_1 = (step_1[0] - 1, step_1[1])
        elif step_1[0] < step_2[0]:
            while step_1[0] <= step_2[0]:
                grid[step_1] = "#"
                step_1 = (step_1[0] + 1, step_1[1])
        elif step_1[1] > step_2[1]:
            while step_1[1] >= step_2[1]:
                grid[step_1] = "#"
                step_1 = (step_1[0], step_1[1] - 1)
        elif step_1[1] < step_2[1]:
            while step_1[1] <= step_2[1]:
                grid[step_1] = "#"
                step_1 = (step_1[0], step_1[1] + 1)

grid_bounds = (
    min(x[0] for x in grid.keys()),
    max(x[0] for x in grid.keys()),
    0,
    max(x[1] for x in grid.keys()),
)

sand_pos = (500, 0)


def print_grid(zoom=False):
    buf = ""
    y_start = grid_bounds[2] if not zoom else sand_pos[1] - 10
    y_end = (grid_bounds[3] + 1) if not zoom else sand_pos[1] + 25
    x_start = grid_bounds[0] - 1
    x_end = grid_bounds[1]
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if (x, y) in grid:
                buf += grid[(x, y)]
            elif (x, y) == sand_pos:
                buf += "+"
            else:
                buf += " "
        buf += "\n"
    os.system("cls")
    print(buf)


ctr = 0
draw = False
abyss_happened = False
while True:
    ctr += 1
    if abyss_happened:
        break
    sand_pos = (500, 0)
    if sand_pos in grid:
        break
    while True:
        if draw:
            print_grid(True)
        if sand_pos[1] > grid_bounds[3]:
            abyss_happened = True
            break
        if (sand_pos[0], sand_pos[1] + 1) not in grid:
            sand_pos = (sand_pos[0], sand_pos[1] + 1)
        elif (sand_pos[0] - 1, sand_pos[1] + 1) not in grid:
            sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
        elif (sand_pos[0] + 1, sand_pos[1] + 1) not in grid:
            sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
        else:
            grid[sand_pos] = "o"
            break
    if abyss_happened:
        True

print(len([x for x in grid.values() if x == "o"]))
print("done")
