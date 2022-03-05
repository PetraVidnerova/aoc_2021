with open("input6", "r") as f:
    numbers = f.read().strip().split(",")
    numbers = list(map(int, numbers))

print(numbers)

fish = {}
for x in numbers:
    fish[x] = fish.get(x, 0) + 1

print(fish)

for _ in range(256):

    count = fish.get(0, 0)
    fish = {
        key-1: value
        for key, value in fish.items()
    }
    fish[6] = fish.get(6, 0) + fish.get(-1, 0)
    fish[-1] = 0
    fish[8] = count
    print(fish)


print(sum(fish.values()))
