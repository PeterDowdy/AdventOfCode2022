data = []
with open("day3.txt") as f:
    data = [x.strip() for x in f.readlines()]

rucksacks = []

shared = []

for n in range(0, len(data), 3):
    first_set = set(data[n])
    second_set = set(data[n + 1])
    third_set = set(data[n + 2])
    shared.append(next(x for x in (first_set & second_set & third_set)))

pass
sum = 0
for s in shared:
    sum += " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s)

print(sum)
