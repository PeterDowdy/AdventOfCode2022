import functools

data = []
with open("day13.txt") as f:
    data = [x.strip() for x in f.readlines()]


data = [eval(x) for x in data if x != ""]

data_pairs = []

for n in range(0, len(data), 2):
    data_pairs.append((data[n], data[n + 1]))


def list_compare(item_one, item_two):
    if len(item_one) and not len(item_two):
        return -1
    elif not len(item_one) and len(item_two):
        return -1
    else:
        for n in range(0, min(len(item_two), len(item_one))):
            if n >= len(item_one):
                return 1
            if n >= len(item_one):
                return -1
            if is_in_order(item_one[n], item_two[n]) == 1:
                return 1
            elif is_in_order(item_one[n], item_two[n]) == -1:
                return -1
        return 1


def is_in_order(item_one, item_two):
    if item_one is None and item_two is None:
        return 1
    if item_one is None and item_two is not None:
        return 1
    if item_one is not None and item_two is None:
        return -1
    if isinstance(item_one, int) and isinstance(item_two, int):
        return 1 if item_one < item_two else 0 if item_one == item_two else -1

    if isinstance(item_one, int):
        item_one = [item_one]
    if isinstance(item_two, int):
        item_two = [item_two]

    for lsub, rsub in zip(item_one, item_two):
        sub = is_in_order(lsub, rsub)
        if sub != 0:
            return sub
    if len(item_one) < len(item_two):
        return 1
    if len(item_one) > len(item_two):
        return -1
    return 0


pairs_with_packet = []
for a, b in data_pairs:
    pairs_with_packet.append(a)
    pairs_with_packet.append(b)

pairs_with_packet.append([[2]])
pairs_with_packet.append([[6]])

correct_order = sorted(
    pairs_with_packet, key=functools.cmp_to_key(is_in_order), reverse=True
)

print((correct_order.index([[2]]) + 1) * (correct_order.index([[6]]) + 1))
