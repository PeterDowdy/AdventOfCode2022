data = []
with open("day5.txt") as f:
    data = [x for x in f.readlines()]

cranes = [[], [], [], [], [], [], [], [], [], []]

crane_rows = data[:8]
for row in crane_rows:
    for n in range(9):
        if row[n * 4 + 1] != " ":
            cranes[n] = [row[n * 4 + 1]] + cranes[n]


instructions = data[10:]

for instruction in instructions:
    tokens = instruction.split()
    amount = int(tokens[1])
    source = int(tokens[3])
    destination = int(tokens[5])

    buf = []
    for n in range(amount):
        if cranes[source - 1]:
            buf = [cranes[source - 1].pop()] + buf
    cranes[destination - 1] = cranes[destination - 1] + buf


for x in cranes:
    if x:
        print(x[-1], end="")
print()
