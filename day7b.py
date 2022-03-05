import numpy as np

with open("input7", "r") as f:
    positions = f.read().strip().split(",")
    positions = list(map(int, positions))

positions = np.array(positions, dtype=int)

start = positions.min()
end = positions.max()


def fuel(pos):
    diff = np.abs(positions - pos)
    fuels = diff * (diff + 1)
    fuels /= 2
    return fuels.sum()


result = 0
minimum = fuel(0)

for pos in range(start, end+1):
    value = fuel(pos)
    if value < minimum:
        minimum = value
        result = pos

print(result)
print(fuel(result))
