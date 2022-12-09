data = []
with open("day9.txt") as f:
    data = [x.strip() for x in f.readlines()]

# data = [
#     x.strip()
#     for x in """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".splitlines()
# ]

visits = {(0, 0)}

chain = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]


def print_map():
    for y in range(-20, 20):
        for x in range(-20, 20):
            if (x, y) == chain[0]:
                print("H", end="")
            elif (x, y) in chain:
                print("T", end="")
            elif (x, y) in visits:
                print("#", end="")
            else:
                print(".", end="")
        print()


def do_follow(head, tail):
    x_dist = head[0] - tail[0]
    y_dist = head[1] - tail[1]
    tail_distance = abs(x_dist) + abs(y_dist)
    if tail_distance > 1:
        if y_dist == 2 and x_dist == 0:
            tail = (tail[0], tail[1] + 1)
        elif y_dist == 2 and x_dist == 1:
            tail = (tail[0] + 1, tail[1] + 1)
        elif y_dist == 2 and x_dist == 2:
            tail = (tail[0] + 1, tail[1] + 1)
        elif y_dist == 1 and x_dist == 2:
            tail = (tail[0] + 1, tail[1] + 1)
        elif y_dist == 0 and x_dist == 2:
            tail = (tail[0] + 1, tail[1])
        elif y_dist == -1 and x_dist == 2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif y_dist == -2 and x_dist == 1:
            tail = (tail[0] + 1, tail[1] - 1)
        elif y_dist == -2 and x_dist == 2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif y_dist == -2 and x_dist == 0:
            tail = (tail[0], tail[1] - 1)
        elif y_dist == -2 and x_dist == -1:
            tail = (tail[0] - 1, tail[1] - 1)
        elif y_dist == -2 and x_dist == -2:
            tail = (tail[0] - 1, tail[1] - 1)
        elif y_dist == -1 and x_dist == -2:
            tail = (tail[0] - 1, tail[1] - 1)
        elif y_dist == 0 and x_dist == -2:
            tail = (tail[0] - 1, tail[1])
        elif y_dist == 1 and x_dist == -2:
            tail = (tail[0] - 1, tail[1] + 1)
        elif y_dist == 2 and x_dist == -1:
            tail = (tail[0] - 1, tail[1] + 1)
        elif y_dist == 2 and x_dist == -2:
            tail = (tail[0] - 1, tail[1] + 1)
    return tail


# print_map()
ctr = 0
for instruction in data:
    ctr += 1
    direction, distance = instruction.split()
    distance = int(distance)
    for n in range(distance):
        current_head = chain[0]
        new_chain = []
        if direction == "U":
            current_head = (current_head[0], current_head[1] - 1)
        elif direction == "R":
            current_head = (current_head[0] + 1, current_head[1])
        elif direction == "D":
            current_head = (current_head[0], current_head[1] + 1)
        elif direction == "L":
            current_head = (current_head[0] - 1, current_head[1])
        new_chain.append(current_head)
        for node in chain[1:]:
            new_chain.append(do_follow(new_chain[-1], node))
        visits.add(new_chain[-1])
        chain = new_chain
        # print_map()

print(len(visits))
