data = []
with open("day11.txt") as f:
    data = [x.strip() for x in f.readlines()]


class Monkey:
    def __init__(self, starting_items, operation, test, if_true, if_false):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = 0


monkeys = [
    Monkey(
        [91, 54, 70, 61, 64, 64, 60, 85], lambda x: x * 13, lambda x: x % 2 == 0, 5, 2
    ),
    Monkey([82], lambda x: x + 7, lambda x: x % 13 == 0, 4, 3),
    Monkey([84, 93, 70], lambda x: x + 2, lambda x: x % 5 == 0, 5, 1),
    Monkey([78, 56, 85, 93], lambda x: x * 2, lambda x: x % 3 == 0, 6, 7),
    Monkey([64, 57, 81, 95, 52, 71, 58], lambda x: x * x, lambda x: x % 11 == 0, 7, 3),
    Monkey([58, 71, 96, 58, 68, 90], lambda x: x + 6, lambda x: x % 17 == 0, 4, 1),
    Monkey([56, 99, 89, 97, 81], lambda x: x + 1, lambda x: x % 7 == 0, 0, 2),
    Monkey([68, 72], lambda x: x + 8, lambda x: x % 19 == 0, 6, 0),
]

for n in range(0, 20):
    for monkey in monkeys:
        for item in monkey.starting_items:
            monkey.inspect_count += 1
            item = monkey.operation(item) // 3
            if monkey.test(item):
                monkeys[monkey.if_true].starting_items.append(item)
            else:
                monkeys[monkey.if_false].starting_items.append(item)
        monkey.starting_items = []


pass
