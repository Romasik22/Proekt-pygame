data = []
with open("xyz.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
print(data[0] + data[1])