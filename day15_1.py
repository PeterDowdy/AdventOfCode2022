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

# for sensor, beacon in sensors_and_beacons:
#     dist = manhattan_distance(sensor, beacon)
#     for y in range(sensor[1] - dist - 1, sensor[1] + dist + 1):
#         for x in range(sensor[0] - dist - 1, sensor[0] + dist + 1):
#             if manhattan_distance((x, y), sensor) <= dist and (x, y) != beacon:
#                 empty_cells.add((x, y))

ctr = 0
for sensor, beacon in sensors_and_beacons:
    ctr += 1
    print(ctr)
    dist = manhattan_distance(sensor, beacon)
    if sensor[1] + dist < 2000000:
        continue
    if sensor[1] - dist > 2000000:
        continue
    for y in range(2000000, 2000001):
        for x in range(sensor[0] - dist - 1, sensor[0] + dist + 1):
            if manhattan_distance((x, y), sensor) <= dist and (x, y) != beacon:
                empty_cells.add((x, y))

print("hi")
