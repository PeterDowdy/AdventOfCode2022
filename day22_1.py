data = []
with open("day22.txt") as f:
    data = [x for x in f.readlines()]

map = {}

cur = None
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


def print_map():
    for y in range(0, len(data) - 1):
        for x in range(0, len(data[y])):
            if (x, y) == cur:
                print(facing, end="")
            elif (x, y) in map:
                print("#" if map[(x, y)] else ".", end="")
            else:
                print(" ", end="")
        print()


for instruction in parsed_instructions:
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
                if facing == ">":
                    next_cur = (min(k[0] for k in map if k[1] == cur[1]), cur[1])
                elif facing == "v":
                    next_cur = (cur[0], min(k[1] for k in map if k[0] == cur[0]))
                elif facing == "<":
                    next_cur = (max(k[0] for k in map if k[1] == cur[1]), cur[1])
                elif facing == "^":
                    next_cur = (cur[0], max(k[1] for k in map if k[0] == cur[0]))
                if map.get(next_cur, None) == True:
                    break
                elif map.get(next_cur, None) == False:
                    cur = next_cur
    ...
final_row = cur[1] + 1
final_col = cur[0] + 1
final_facing = 0 if facing == ">" else 1 if facing == "v" else 2 if facing == "<" else 3

print(1000 * final_row + 4 * final_col + final_facing)
