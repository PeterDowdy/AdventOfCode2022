data = []
with open("day3.txt") as f:
    data = [x.strip() for x in f.readlines()]

rucksacks = []

shared = []

for rucksack_raw in data:
    first, second = (
        rucksack_raw[0 : len(rucksack_raw) // 2],
        rucksack_raw[len(rucksack_raw) // 2 :],
    )
    rucksacks.append((first, second))
    first_set = set(first)
    second_set = set(second)
    shared.append(next(x for x in (first_set & second_set)))

pass
sum = 0
for s in shared:
    sum += " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s)

print(sum)
