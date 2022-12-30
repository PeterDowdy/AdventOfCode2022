data = []
with open("day22.txt") as f:
    data = [x for x in f.readlines()]

map = {}

cur = None
next_cur = None
facing = ">"

for y in range(0, len(data) - 1):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            map[(x, y)] = True
        elif data[y][x] == ".":
            if cur is None:
                cur = (x, y)
            map[(x, y)] = False

instructions = data[-1]

"""
_01
_2_
34_
5__

2 is the bottom, 5 is the top
"""

parsed_instructions = []
buf = ""
for n in instructions:
    if n not in ["L", "R"]:
        buf += n
    else:
        parsed_instructions.append(int(buf))
        buf = ""
        parsed_instructions.append(n)
if buf:
    parsed_instructions.append(int(buf))

visits = set()


def print_map():
    for y in range(0, len(data) - 1):
        for x in range(0, len(data[y])):
            if (x, y) == cur:
                print("\033[31m" + facing + "\033[0m", end="")
            elif (x, y) == next_cur:
                print(
                    "\033[32m" + ("#" if map[(x, y)] else next_facing) + "\033[0m",
                    end="",
                )
            elif (x, y) in map:
                to_write = "#" if map[(x, y)] else "."
                if (x, y) in visits:
                    to_write = "\033[34m" + to_write + "\033[0m"
                print(to_write, end="")
            else:
                print(" ", end="")
        print()


cube_wraps = 0
for instruction in parsed_instructions:
    visits.add(cur)
    if instruction == "R":
        if facing == ">":
            facing = "v"
        elif facing == "v":
            facing = "<"
        elif facing == "<":
            facing = "^"
        elif facing == "^":
            facing = ">"
    elif instruction == "L":
        if facing == ">":
            facing = "^"
        elif facing == "v":
            facing = ">"
        elif facing == "<":
            facing = "v"
        elif facing == "^":
            facing = "<"
    else:
        for n in range(0, instruction):
            visits.add(cur)
            if facing == ">":
                next_cur = (cur[0] + 1, cur[1])
            elif facing == "v":
                next_cur = (cur[0], cur[1] + 1)
            elif facing == "<":
                next_cur = (cur[0] - 1, cur[1])
            elif facing == "^":
                next_cur = (cur[0], cur[1] - 1)
            if map.get(next_cur, None) == True:
                break
            elif map.get(next_cur, None) == False:
                cur = next_cur
            else:
                cube_wraps += 1
                next_facing = None
                next_cur = None
                ...
                if facing == ">":
                    if cur[0] == 149:  # 1->4 # verifiedx3
                        next_facing = "<"
                        next_cur = (99, 150 - cur[1] - 1)
                    elif cur[0] == 99 and cur[1] < 100:  # 2->1 verifiedx3
                        next_facing = "^"
                        next_cur = (100 + (cur[1] - 50), 49)
                    elif cur[0] == 99:  # 4->1 verifiedx3
                        next_facing = "<"
                        next_cur = (149, (150 - cur[1]) - 1)
                    else:  # 5 -> 4 verifiedx3
                        next_facing = "^"
                        next_cur = (50 + (cur[1] - 150), 149)
                elif facing == "v":
                    if cur[1] == 49:  # 1->2 verifiedx3
                        next_facing = "<"
                        next_cur = (99, 50 + (cur[0] - 100))
                    elif cur[1] == 149:  # 4->5 verifiedx3
                        next_facing = "<"
                        next_cur = (49, 150 + (cur[0] - 50))
                    elif cur[1] == 199:  # 5- > 1 # verifiedx3
                        next_facing = "v"
                        next_cur = (100 + cur[0], 0)
                elif facing == "<":
                    if cur[0] == 50 and cur[1] < 50:  # 0->3 verifiedx3
                        next_facing = ">"
                        next_cur = (0, 150 - cur[1] - 1)
                    elif cur[0] == 50:  # 2->3 verifiedx3
                        next_facing = "v"
                        next_cur = (cur[1] - 50, 100)
                    elif cur[0] == 0 and cur[1] < 150:  # 3->0 verifiedx3
                        next_facing = ">"
                        next_cur = (50, 150 - cur[1] - 1)
                    elif cur[0] == 0:  # 5->1: verifiedx3
                        next_facing = "v"
                        next_cur = (50 + cur[1] - 150, 0)
                elif facing == "^":
                    if cur[1] == 0 and cur[0] < 100:  # 0 -> 5  verifiedx3
                        next_facing = ">"
                        next_cur = (0, 150 + (cur[0] - 50))
                    elif cur[1] == 0:  # 1->5 verifiedx3
                        next_facing = "^"
                        next_cur = ((cur[0]) - 100, 199)
                    elif cur[1] == 100:  # 3 -> 2 verifiedx3
                        next_facing = ">"
                        next_cur = (50, 50 + cur[0])
                ...
                if map.get(next_cur, None) == True:
                    break
                elif map.get(next_cur, None) == False:
                    visits.add(cur)
                    cur = next_cur
                    facing = next_facing

    ...
final_row = cur[1] + 1
final_col = cur[0] + 1
final_facing = 0 if facing == ">" else 1 if facing == "v" else 2 if facing == "<" else 3

print(1000 * final_row + 4 * final_col + final_facing)
