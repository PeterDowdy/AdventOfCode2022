from itertools import permutations

data = []
with open("day16.txt") as f:
    data = [x.strip() for x in f.readlines()]


class Valve:
    def __init__(self, name, value, connections):
        self.name = name
        self.value = value
        self.connections = connections

    def get_net_pressure(self, remaining_time):
        return self.value * remaining_time


valves = {}

for line in data:
    parts = line.split(" ")
    valve_name = parts[1]
    rate = int(parts[4].split("=")[-1].replace(";", ""))
    connections = [x.replace(",", "") for x in parts[9:]]
    valves[valve_name] = Valve(valve_name, rate, connections)


def get_best_estimated_pressure(remaining, route):
    p = 0
    for v in sorted(route, key=lambda x: x.value, reverse=True):
        p += v.get_net_pressure(remaining - 1)
        remaining -= 2
    return p


def find_connectors(start, end):
    paths = [[start]]
    successes = []
    while paths:
        top_path = paths.pop(0)
        current_position = valves[top_path[-1]]
        if current_position.name == end:
            successes.append(top_path)
            continue
        for connection in current_position.connections:
            if connection in top_path:
                continue
            paths.append(top_path + [connection])
    return list(sorted(successes, key=lambda x: len(x)))[0][1:]


paths = [(30, 0, "AA", [])]
best_so_far = 0
while paths:
    top_path = paths.pop(0)
    remaining, pressure, this_node, open_valves = top_path

    if pressure > best_so_far:
        best_so_far = pressure
        print(f"new best: {best_so_far} - {len(paths)} remaining")

    if remaining == 0:
        continue

    best_possible_remaining_pressure = pressure + get_best_estimated_pressure(
        remaining,
        [v for v in valves.values() if v.name not in open_valves and not v.value == 0],
    )

    if best_possible_remaining_pressure < best_so_far:
        continue

    next_routes = []

    for k, v in valves.items():
        if k in open_valves:
            continue
        if v.value == 0:
            continue
        cxn = find_connectors(this_node, k)
        next_routes.append(
            (pressure + v.get_net_pressure(remaining - len(cxn) - 1), len(cxn), cxn)
        )

    for extra_pressure, distance, route in next_routes:
        if remaining - distance < 0:
            continue
        paths.append(
            (
                remaining - distance - 1,
                extra_pressure,
                route[-1],
                open_valves.copy() + [route[-1]],
            )
        )

    if remaining == 0 or not next_routes:
        continue

    paths = sorted(paths, key=lambda x: x[1], reverse=True)

print(best_so_far)
