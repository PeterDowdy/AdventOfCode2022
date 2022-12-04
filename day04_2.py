data = []
with open("day4.txt") as f:
    data = [x.strip() for x in f.readlines()]


any_overlap = 0

for assignment in data:
    first, second = assignment.split(",")
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    first_start = int(first_start)
    first_end = int(first_end)
    second_start = int(second_start)
    second_end = int(second_end)

    first_set = set([x for x in range(first_start, first_end + 1)])
    second_set = set([x for x in range(second_start, second_end + 1)])

    if len(first_set & second_set) > 0:
        any_overlap += 1

print(any_overlap)
