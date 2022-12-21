data = []
with open("day21.txt") as f:
    data = [x.strip() for x in f.readlines()]

monkies = {}

for row in data:
    tokens = row.split(":")
    monkey = tokens[0]
    rules = tokens[1].strip().split(" ")
    if len(rules) == 1:
        monkies[monkey] = (int(rules[0]), None)
    else:
        monkies[monkey] = (None, rules)

monkey_found = False
while not monkey_found:
    for monkey, rules in monkies.items():
        value, math = rules
        if monkey == "root" and value:
            print(value)
            monkey_found = True
            break
        if value:
            continue
        else:
            left_val, _ = monkies[math[0]]
            right_val, _ = monkies[math[2]]
            if not left_val or not right_val:
                continue
            if math[1] == "+":
                monkies[monkey] = (left_val + right_val, None)
            elif math[1] == "*":
                monkies[monkey] = (left_val * right_val, None)
            elif math[1] == "/":
                monkies[monkey] = (left_val // right_val, None)
            elif math[1] == "-":
                monkies[monkey] = (left_val - right_val, None)
