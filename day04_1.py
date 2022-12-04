data = []
with open("day4.txt") as f:
    data = [x.strip() for x in f.readlines()]


fully_contains = 0

for assignment in data:
    first, second = assignment.split(",")
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    first_start = int(first_start)
    first_end = int(first_end)
    second_start = int(second_start)
    second_end = int(second_end)

    if first_start <= second_start and first_end >= second_end:
        fully_contains += 1
    elif second_start <= first_start and second_end >= first_end:
        fully_contains += 1

print(fully_contains)
