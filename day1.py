count = 0
previous = None
with open("input", "r") as f:
    for line in f:
        current = int(line)
        if previous is None:
            previous = current
            continue
        if current > previous:
            count += 1
        previous = current

print(count)
