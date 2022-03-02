counts = None
lines = 0
with open("input3", "r") as f:
    for line in f:
        line = line.strip()
        if counts is None:
            counts = { i: 0 for i, _ in enumerate(line) } 
        for i, digit in enumerate(line):
            if digit == "1":
                counts[i] += 1 
        lines += 1
        
gamma = ""
epsilon = ""

for i in range(len(counts.keys())):
    if counts[i] > lines / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma, int(gamma, 2))
print(epsilon, int(epsilon, 2))


print(int(gamma, 2)*int(epsilon, 2))
