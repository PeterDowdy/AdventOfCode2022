data = []
with open("day8.txt") as f:
    data = [x.strip() for x in f.readlines()]

grid = {}
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        grid[(x, y)] = int(data[y][x])

visibility_scores = {}

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        this_cell = grid[(x, y)]
        w_ctr = 0
        for n in range(x - 1, -1, -1):
            w_ctr += 1
            if grid[(n, y)] >= this_cell:
                break
        e_ctr = 0
        for n in range(x + 1, len(data[y])):
            e_ctr += 1
            if grid[(n, y)] >= this_cell:
                break
        n_ctr = 0
        for n in range(y - 1, -1, -1):
            n_ctr += 1
            if grid[(x, n)] >= this_cell:
                break
        s_ctr = 0
        for n in range(y + 1, len(data)):
            s_ctr += 1
            if grid[(x, n)] >= this_cell:
                break
        visibility_scores[(x, y)] = w_ctr * e_ctr * s_ctr * n_ctr


print(max(list(visibility_scores.values())))
