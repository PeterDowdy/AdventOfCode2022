from collections import Counter
from functools import cache


data = []
with open("day17.txt") as f:
    data = [x.strip() for x in f.readlines()][0]

# data = [x for x in ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]
pieces = [
    frozenset([(2, 0), (3, 0), (4, 0), (5, 0)]),
    frozenset([(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)]),
    frozenset([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)]),
    frozenset([(2, 0), (2, 1), (2, 2), (2, 3)]),
    frozenset([(2, 0), (3, 0), (2, 1), (3, 1)]),
]


rock_len = len(pieces)
gust_len = len(data)


blocked_cells = frozenset()

stop_at = 2022
# stop_at = 2022
stop_at = 1000000000000


def print_map(blocked_cells, active_rock):
    print()
    peak = find_peak(blocked_cells)
    for y in range(peak + 8, -1, -1):
        for x in range(0, 7):
            if (x, y) in blocked_cells:
                print("#", end="")
            elif (x, y) in active_rock:
                print("@", end="")
            else:
                print(".", end="")
        print()


@cache
def find_peak(blocked_cells):
    peak = -1
    for k in blocked_cells:
        if k[1] > peak:
            peak = k[1]
    return peak + 1


@cache
def add_rock_to_map(blocked_cells, rock):
    map_peak = find_peak(blocked_cells)
    added_rock = []
    for k in rock:
        added_rock.append((k[0], k[1] + map_peak + 3))
    return frozenset(added_rock)


@cache
def shave_blocked_cells(blocked_cells):
    sub_map = []

    flood_search = [(0, find_peak(blocked_cells) + 1)]
    flood_seen = set()

    while flood_search:
        x, y = flood_search.pop()
        if (x, y) in flood_seen:
            continue
        flood_seen.add((x, y))
        if y < 0:
            continue
        if x < 0:
            continue
        if x > 6:
            continue
        if (x, y) in blocked_cells:
            sub_map.append((x, y))
        else:
            for dx, dy in [(1, 0), (-1, 0), (0, -1)]:
                if (x + dx, y + dy) in flood_seen:
                    continue

                flood_search.append((x + dx, y + dy))

    sub_max_y = min(x[1] for x in sub_map)
    sub_map = frozenset((x, y - sub_max_y) for x, y in sub_map)

    return frozenset(sub_map)


seen_calls = {}


@cache
def next_frame(blocked_cells, rock_ctr, gust_ctr):
    active_rock = add_rock_to_map(blocked_cells, pieces[rock_ctr])
    rock_ctr += 1
    if rock_ctr == rock_len:
        rock_ctr = 0

    while True:
        gust = data[gust_ctr]
        gust_ctr += 1
        if gust_ctr == gust_len:
            gust_ctr = 0
        if gust == ">":
            next_rock = frozenset((x + 1, y) for x, y in active_rock)
        else:
            next_rock = frozenset((x - 1, y) for x, y in active_rock)
        if (
            all(x not in blocked_cells for x in next_rock)
            and not any(x[0] == 7 for x in next_rock)
            and not any(x[0] < 0 for x in next_rock)
        ):
            active_rock = next_rock

        next_rock = frozenset((x, y - 1) for x, y in active_rock)
        if (
            any(x in blocked_cells for x in next_rock)
            or max(x[1] for x in next_rock) < 0
        ):
            blocked_cells = blocked_cells | active_rock
            shaved_blocked_cells = shave_blocked_cells(blocked_cells)
            return (
                max(x[1] for x in blocked_cells)
                - max(x[1] for x in shaved_blocked_cells),
                shaved_blocked_cells,
                rock_ctr,
                gust_ctr,
            )
        else:
            active_rock = next_rock
            continue


def print_cache_stats():
    print(
        f"""
    next_frame: {next_frame.cache_info().hits}
    add_rock_to_map: {add_rock_to_map.cache_info().hits}
    find_peak: {find_peak.cache_info().hits}
    shave_blocked_cells: {shave_blocked_cells.cache_info().hits}
"""
    )


heights = []
height_shavings = 0

rock_ctr = 0
gust_ctr = 0
active_rock = None
rock_count = 0
ctr = 0
rock_size = 0
total_height = 0
final_mode = False
while ctr < stop_at:
    ctr += 1
    if not final_mode and (blocked_cells, rock_ctr, gust_ctr) in seen_calls:
        final_mode = True
        start_offset = seen_calls[(blocked_cells, rock_ctr, gust_ctr)]
        delta = ctr - start_offset
        delta_height = heights[-1] - heights[start_offset]
        remainder = (stop_at - (ctr)) // delta
        total_height += remainder * delta_height
        ctr += remainder * delta
    seen_calls[(blocked_cells, rock_ctr, gust_ctr)] = ctr
    next_height, blocked_cells, rock_ctr, gust_ctr = next_frame(
        blocked_cells, rock_ctr, gust_ctr
    )
    total_height += next_height
    heights.append(total_height)

tower_height = total_height + max(x[1] for x in blocked_cells) + 1

print(f"The tower is {tower_height} blocks high.")
