data = None
with open("day6.txt") as f:
    data = f.read()

for n in range(14, len(data)):
    if len(set(data[n - 14 : n])) == 14:
        print(data[n - 14 : n])
        print(n)
        break
