with open("input6", "r") as f:
    numbers = f.read().strip().split(",")
    numbers = list(map(int, numbers))

print(numbers)

for _ in range(80):
    count = sum([x == 0 for x in numbers])
    numbers = [
        x-1 if x > 0 else 6
        for x in numbers
    ]
    numbers.extend([8]*count)
    print(numbers)

print(len(numbers))
