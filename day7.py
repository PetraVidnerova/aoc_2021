import numpy as np

with open("input7", "r") as f:
    positions = f.read().strip().split(",")
    positions = list(map(int, positions))

positions = np.array(positions, dtype=int)

# start = positions.min()
# end = positions.max()

# result = 0
# minimum = positions.sum()

# for pos in range(start, end+1):
#     value = np.abs(positions - pos).sum()
#     if value < minimum:
#         minimum = value
#         result = pos

result = np.median(positions)

print(result)

print(np.sum(np.abs(positions - result)))
