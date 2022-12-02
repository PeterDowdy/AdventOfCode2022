data = []
with open("day1.txt") as f:
    data = [x.strip() for x in f.read().split("\n\n")]

elf_groups = [x.split() for x in data]

elf_counts = [[int(y) for y in x] for x in elf_groups]

elf_sums = [sum(x) for x in elf_counts]

print(sorted(elf_sums)[-1] + sorted(elf_sums)[-2] + sorted(elf_sums)[-3])
