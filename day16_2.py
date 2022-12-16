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


paths = [(26, 0, "AA", 0, "AA", 0, [])]
best_so_far = 0
while paths:
    top_path = paths.pop(0)
    (
        remaining,
        pressure,
        me_node,
        me_move_buf,
        elephant_node,
        elephant_move_buf,
        open_valves,
    ) = top_path

    while me_move_buf and elephant_move_buf:
        remaining -= 1
        me_move_buf -= 1
        elephant_move_buf -= 1

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

    me_candidates = []
    elephant_candidates = []

    me_next_routes = []

    for k, v in valves.items():
        if k in open_valves:
            continue
        if v.value == 0:
            continue
        cxn = find_connectors(me_node, k)
        me_next_routes.append(
            (v.get_net_pressure(remaining - len(cxn) - 1), len(cxn) + 1, cxn)
        )

    for extra_pressure, distance, route in me_next_routes:
        if remaining - (me_move_buf + distance) < 0:
            continue
        me_candidates.append((distance, extra_pressure, route[-1]))

    elephant_next_routes = []

    for k, v in valves.items():
        if k in open_valves:
            continue
        if v.value == 0:
            continue
        cxn = find_connectors(elephant_node, k)
        elephant_next_routes.append(
            (v.get_net_pressure(remaining - len(cxn) - 1), len(cxn) + 1, cxn)
        )

    for extra_pressure, distance, route in elephant_next_routes:
        if remaining - (elephant_move_buf + distance) < 0:
            continue
        elephant_candidates.append((distance, extra_pressure, route[-1]))

    if (
        me_next_routes
        and elephant_next_routes
        and not me_move_buf
        and not elephant_move_buf
    ):
        for me_dist, me_pressure, me_node in me_candidates:
            for e_dist, e_pressure, e_node in elephant_candidates:
                if me_node == e_node:
                    continue
                paths.append(
                    (
                        remaining,
                        pressure + me_pressure + e_pressure,
                        me_node,
                        me_dist,
                        e_node,
                        e_dist,
                        open_valves.copy() + [me_node, e_node],
                    )
                )
    elif me_next_routes and not me_move_buf:
        for me_dist, me_pressure, me_node in me_candidates:
            paths.append(
                (
                    remaining,
                    pressure + me_pressure,
                    me_node,
                    me_dist,
                    elephant_node,
                    elephant_move_buf,
                    open_valves.copy() + [me_node],
                )
            )
    elif elephant_next_routes and not elephant_move_buf:
        for e_dist, e_pressure, e_node in elephant_candidates:
            paths.append(
                (
                    remaining,
                    pressure + e_pressure,
                    me_node,
                    me_move_buf,
                    e_node,
                    e_dist,
                    open_valves.copy() + [e_node],
                )
            )

    if remaining == 0 or (not me_next_routes and not elephant_next_routes):
        continue

    paths = sorted(paths, key=lambda x: x[1], reverse=True)

print(best_so_far)
