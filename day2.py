x = 0
d = 0
with open("input2", "r") as f:
    for line in f:
        command, number = line.split(" ")
        number = int(number)

        if command == "forward":
            x += number
        elif command == "down":
            d += number
        elif command == "up":
            d -= number
        else:
            raise ValueError("unknown command")

print(x*d)
