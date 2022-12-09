data = []
with open("day9.txt") as f:
    data = [x.strip() for x in f.readlines()]

# data = [
#     x.strip()
#     for x in """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".splitlines()
# ]

visits = {(0, 0)}

current_head = (0, 0)
current_tail = (0, 0)


def print_map():
    for y in range(-20, 20):
        for x in range(-20, 20):
            if (x, y) == current_head:
                print("H", end="")
            elif (x, y) == current_tail:
                print("T", end="")
            elif (x, y) in visits:
                print("#", end="")
            else:
                print(".", end="")
        print()


# print_map()
ctr = 0
for instruction in data:
    ctr += 1
    print(instruction)
    direction, distance = instruction.split()
    distance = int(distance)
    for n in range(distance):
        if direction == "U":
            current_head = (current_head[0], current_head[1] - 1)
        elif direction == "R":
            current_head = (current_head[0] + 1, current_head[1])
        elif direction == "D":
            current_head = (current_head[0], current_head[1] + 1)
        elif direction == "L":
            current_head = (current_head[0] - 1, current_head[1])
        x_dist = current_head[0] - current_tail[0]
        y_dist = current_head[1] - current_tail[1]
        tail_distance = abs(x_dist) + abs(y_dist)
        if tail_distance > 1:
            if y_dist == 2 and x_dist == 0:
                current_tail = (current_tail[0], current_tail[1] + 1)
            elif y_dist == 2 and x_dist == 1:
                current_tail = (current_tail[0] + 1, current_tail[1] + 1)
            elif y_dist == 1 and x_dist == 2:
                current_tail = (current_tail[0] + 1, current_tail[1] + 1)
            elif y_dist == 0 and x_dist == 2:
                current_tail = (current_tail[0] + 1, current_tail[1])
            elif y_dist == -1 and x_dist == 2:
                current_tail = (current_tail[0] + 1, current_tail[1] - 1)
            elif y_dist == -2 and x_dist == 1:
                current_tail = (current_tail[0] + 1, current_tail[1] - 1)
            elif y_dist == -2 and x_dist == 0:
                current_tail = (current_tail[0], current_tail[1] - 1)
            elif y_dist == -2 and x_dist == -1:
                current_tail = (current_tail[0] - 1, current_tail[1] - 1)
            elif y_dist == -1 and x_dist == -2:
                current_tail = (current_tail[0] - 1, current_tail[1] - 1)
            elif y_dist == 0 and x_dist == -2:
                current_tail = (current_tail[0] - 1, current_tail[1])
            elif y_dist == 1 and x_dist == -2:
                current_tail = (current_tail[0] - 1, current_tail[1] + 1)
            elif y_dist == 2 and x_dist == -1:
                current_tail = (current_tail[0] - 1, current_tail[1] + 1)
        visits.add(current_tail)
        # print_map()

print(len(visits))
