field_dict = {}

with open("input5", "r") as f:

    for line in f:
        start, end = line.strip().split("->")
        start = start.split(",")
        end = end.split(",")
        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]
        print(start, end)

        if start[0] == end[0]:
            if start[1] > end[1]:
                start[1], end[1] = end[1], start[1]
            for i in range(start[1], end[1]+1):
                field_dict[(start[0], i)] = field_dict.get(
                    (start[0], i), 0) + 1
        elif start[1] == end[1]:
            if start[0] > end[0]:
                start[0], end[0] = end[0], start[0]
            for i in range(start[0], end[0]+1):
                field_dict[(i, start[1])] = field_dict.get(
                    (i, start[1]), 0) + 1

print(field_dict)

total = 0
for val in field_dict.values():
    if val >= 2:
        total += 1

print(total)
