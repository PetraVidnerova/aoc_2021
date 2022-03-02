x = 0
d = 0
aim = 0

with open("input2", "r") as f:
    for line in f:
        command, number = line.split(" ")
        number = int(number)

        if command == "forward":
            x += number
            d += aim * number 
        elif command == "down":
            aim += number
        elif command == "up":
            aim -= number
        else:
            raise ValueError("unknown command")

print(x*d)
