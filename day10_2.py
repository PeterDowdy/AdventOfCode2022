data = []
with open("day10.txt") as f:
    data = [x.strip() for x in f.readlines()]

signal_strength = 0

lines = []
line = ""

x = 1
inst_buf = []
cycle = 0
scanline = 0
for instr in data:
    cycle += 1
    if instr == "noop":
        inst_buf.append(0)
    else:
        command, amount = instr.split(" ")
        amount = int(amount)
        inst_buf.append(0)
        inst_buf.append(amount)
    if x == scanline or (x - 1) == scanline or (x + 1) == scanline:
        line += "#"
    else:
        line += "."
    if inst_buf:
        x += inst_buf[0]
        inst_buf = inst_buf[1:]
    scanline += 1
    if scanline and not scanline % 40:
        lines.append(line)
        line = ""
        scanline = 0

for c in inst_buf:
    cycle += 1
    if x == scanline or (x - 1) == scanline or (x + 1) == scanline:
        line += "#"
    else:
        line += "."
    x += c
    inst_buf = inst_buf[1:]
    scanline += 1
    if scanline and not cycle % 40:
        lines.append(line)
        line = ""
        scanline = 0


lines.append(line)
for line in lines:
    print(line)
