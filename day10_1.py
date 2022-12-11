data = []
with open("day10.txt") as f:
    data = [x.strip() for x in f.readlines()]

signal_strength = 0

x = 1
inst_buf = []
cycle = 0
for instr in data:
    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strength += x * cycle
    if instr == "noop":
        inst_buf.append(0)
    else:
        command, amount = instr.split(" ")
        amount = int(amount)
        inst_buf.append(0)
        inst_buf.append(amount)
    if inst_buf:
        x += inst_buf[0]
        inst_buf = inst_buf[1:]

for c in inst_buf:
    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strength += x * cycle
    x += c
    inst_buf = inst_buf[1:]


print(signal_strength)
