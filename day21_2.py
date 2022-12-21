from sympy import symbols, Eq, solve, parse_expr

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

left_goal, _, right_goal = monkies["root"][1]

monkies["humn"] = ("humn", None)


def perform_monkey(left_val, operator, right_val):
    if operator == "+":
        return left_val + right_val
    elif operator == "*":
        return left_val * right_val
    elif operator == "/":
        return left_val // right_val
    elif operator == "-":
        return left_val - right_val


def resolve_monkey_math(monkey):
    val, math = monkey
    if val:
        return val

    l, o, r = math
    if isinstance(l, int) and isinstance(r, int):
        return f"{perform_monkey(l,o,r)}"

    return f"({resolve_monkey_math(monkies[l])}{o}{resolve_monkey_math(monkies[r])})"


left_math = resolve_monkey_math(monkies[left_goal])

right_math = int(eval(resolve_monkey_math(monkies[right_goal])))

humn = symbols("humn")
expr = parse_expr(left_math)
sol = solve(Eq(expr, right_math), humn)

print(sol)
pass
