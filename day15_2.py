data = []
with open("day15.txt") as f:
    data = [x.strip() for x in f.readlines()]

sensors_and_beacons = []
for row in data:
    sensor, beacon = row.split(":")
    sensor = sensor.split(" ")[-2:]
    beacon = beacon.split(" ")[-2:]
    sensor = (
        int(sensor[0].split("=")[1].replace(",", "")),
        int(sensor[1].split("=")[1]),
    )
    beacon = (
        int(beacon[0].split("=")[1].replace(",", "")),
        int(beacon[1].split("=")[1]),
    )
    sensors_and_beacons.append((sensor, beacon))


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


empty_cells = set()
beacon_cells = set()
sensor_cells = set()

# for sensor, beacon in sensors_and_beacons:
#     sensor_cells.add(sensor)
#     dist = manhattan_distance(sensor, beacon)
#     for y in range(sensor[1] - dist - 1, sensor[1] + dist + 1):
#         for x in range(sensor[0] - dist - 1, sensor[0] + dist + 1):
#             if manhattan_distance((x, y), sensor) <= dist and (x, y) != beacon:
#                 empty_cells.add((x, y))
#             elif (x, y) == beacon:
#                 beacon_cells.add((x, y))

# ctr = 0
# for sensor, beacon in sensors_and_beacons:
#     ctr += 1
#     print(ctr)
#     dist = manhattan_distance(sensor, beacon)
#     if sensor[1] + dist < 2000000:
#         continue
#     if sensor[1] - dist > 2000000:
#         continue
#     for y in range(max(sensor[0] - dist - 1,0), min(sensor[0] + dist + 1,4000000)):
#         for x in range(max(sensor[0] - dist - 1, 0), min(sensor[0] + dist + 1, 4000000)):
#             if manhattan_distance((x, y), sensor) <= dist and (x, y) != beacon:
#                 empty_cells.add((x, y))


# ctr = 0
# for sensor, beacon in sensors_and_beacons:
#     ctr += 1
#     print(ctr)
#     dist = manhattan_distance(sensor, beacon)
#     for y in range(max(sensor[0] - dist - 1, 0), min(sensor[0] + dist + 1, 20)):
#         for x in range(max(sensor[0] - dist - 1, 0), min(sensor[0] + dist + 1, 20)):
#             if manhattan_distance((x, y), sensor) <= dist and (x, y) != beacon:
#                 empty_cells.add((x, y))


candidate_spots = set()


def win(pt):
    if not all(
        manhattan_distance(pt, s) > manhattan_distance(s, b)
        for s, b in sensors_and_beacons
    ):
        pass
    else:
        print(pt)
        print(pt[0] * 4000000 + pt[1])
        print("win")


ctr = 0
for sensor, beacon in sensors_and_beacons:
    ctr += 1
    print(ctr)
    dist = manhattan_distance(sensor, beacon)
    y = sensor[1] - dist
    x = sensor[0]
    if (x, y - 1) in candidate_spots:
        win((x, y - 1))
    candidate_spots.add((x, y - 1))
    while x >= sensor[0] - dist:
        if (x - 1, y) in candidate_spots:
            win((x - 1, y))
        candidate_spots.add((x - 1, y))
        x -= 1
        y += 1
        if x < 0 or x > 4000000 or y < 0 or y > 4000000:
            break
    y = sensor[1]
    x = sensor[0] - dist
    if (x - 1, y) in candidate_spots:
        win((x - 1, y))
    candidate_spots.add((x - 1, y))
    while y <= sensor[1] + dist:
        if (x, y + 1) in candidate_spots:
            win((x, y + 1))
        candidate_spots.add((x, y + 1))
        x += 1
        y += 1
        if x < 0 or x > 4000000 or y < 0 or y > 4000000:
            break
    y = sensor[1] + dist
    x = sensor[0]
    if (x, y + 1) in candidate_spots:
        win((x, y + 1))
    candidate_spots.add((x, y + 1))
    while x <= sensor[0] + dist:
        if (x + 1, y) in candidate_spots:
            win((x + 1, y))
        candidate_spots.add((x + 1, y))
        x += 1
        y -= 1
        if x < 0 or x > 4000000 or y < 0 or y > 4000000:
            break
    y = sensor[1]
    x = sensor[0] + dist
    if (x + 1, y) in candidate_spots:
        win((x + 1, y))
    candidate_spots.add((x + 1, y))
    while y >= sensor[1] - dist:
        if (x, y - 1) in candidate_spots:
            win((x, y - 1))
        candidate_spots.add((x, y - 1))
        x -= 1
        y -= 1
        if x < 0 or x > 4000000 or y < 0 or y > 4000000:
            break
    print("got points")

print("done")
