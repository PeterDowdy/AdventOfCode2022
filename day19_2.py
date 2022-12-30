data = []
with open("day19.txt") as f:
    data = [x.strip() for x in f.readlines()]

blueprints = []

for row in data[:3]:
    toks = row.replace(":", "").split(" ")
    blueprints.append(
        {
            "ore": (int(toks[6]), 0, 0),
            "clay": (int(toks[12]), 0, 0),
            "obsidian": (int(toks[18]), int(toks[21]), 0),
            "geode": (int(toks[27]), 0, int(toks[30])),
        }
    )

# blueprints = [
#     {
#         "ore": (4, 0, 0),
#         "clay": (2, 0, 0),
#         "obsidian": (3, 14, 0),
#         "geode": (2, 0, 7),
#     },
#     {
#         "ore": (2, 0, 0),
#         "clay": (3, 0, 0),
#         "obsidian": (3, 8, 0),
#         "geode": (3, 0, 12),
#     },
# ]


def get_robot_next_move(search, robot, cost):
    (
        minutes,
        ore,
        clay,
        obsidian,
        geodes,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ) = search
    ore_cost, clay_cost, obsidian_cost = cost
    if ore_cost <= ore and clay_cost <= clay and obsidian_cost <= obsidian:
        return (
            minutes + 1,
            ore_robots + ore - ore_cost,
            clay_robots + clay - clay_cost,
            obsidian_robots + obsidian - obsidian_cost,
            geode_robots + geodes,
            ore_robots + 1 if robot == "ore" else ore_robots,
            clay_robots + 1 if robot == "clay" else clay_robots,
            obsidian_robots + 1 if robot == "obsidian" else obsidian_robots,
            geode_robots + 1 if robot == "geode" else geode_robots,
        )


def find_most_geodes(blueprint):
    max_geodes = 0
    max_geodes_by_turn = {}

    searches = [(1, 0, 0, 0, 0, 1, 0, 0, 0)]

    while searches:
        search = searches.pop(0)
        (
            minutes,
            ore,
            clay,
            obsidian,
            geodes,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        ) = search
        if minutes == 33:
            max_geodes = max(max_geodes, geodes)
            continue
        max_possible_geodes = (
            geodes
            + sum([x for x in range(0, 33 - minutes)])
            + (33 - minutes) * geode_robots
        )
        if (
            minutes not in max_geodes_by_turn
            or max_possible_geodes > max_geodes_by_turn[minutes]
        ):
            max_geodes_by_turn[minutes] = max_possible_geodes
        if max_geodes_by_turn[minutes] > max_possible_geodes:
            continue

        add_geode = get_robot_next_move(search, "geode", blueprint["geode"])
        if add_geode:
            searches.append(add_geode)
            continue
        add_obsidian = get_robot_next_move(search, "obsidian", blueprint["obsidian"])
        if add_obsidian and obsidian_robots < blueprint["geode"][2]:
            searches.append(add_obsidian)
        add_clay = get_robot_next_move(search, "clay", blueprint["clay"])
        if add_clay and clay_robots < blueprint["obsidian"][1]:
            searches.append(add_clay)
        add_ore = get_robot_next_move(search, "ore", blueprint["ore"])
        if add_ore and ore_robots < max(x[0] for x in blueprint.values()):
            searches.append(add_ore)

        if not add_obsidian or not add_clay or not add_ore:
            searches.append(
                (
                    minutes + 1,
                    ore + ore_robots,
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    geodes + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                )
            )
        searches = sorted(
            searches, key=lambda x: (x[8], x[7], x[6], x[5]), reverse=True
        )
    return max_geodes


geodes = []

for ix, b in enumerate(blueprints):
    print(f"Blueprint {ix+1}", end="")
    most_geodes = find_most_geodes(b)
    print(f": {most_geodes}")

    geodes.append(most_geodes)

product_geodes = 1
for g in geodes:
    product_geodes *= g

print(product_geodes)
