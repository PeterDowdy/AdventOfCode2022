data = None
with open("day6.txt") as f:
    data = f.read()

for n in range(4, len(data)):
    if len(set(data[n - 4 : n])) == 4:
        print(data[n - 4 : n])
        print(n)
        break
