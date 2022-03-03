lines = 0
numbers = []
with open("input3", "r") as f:
    for line in f:
        line = line.strip()
        numbers.append(line)
        lines += 1

oxygen = ""
co2 = ""

bits_len = len(numbers[0])


for i in range(bits_len):
    count_o = 0
    lines_o = 0
    count_c = 0
    lines_c = 0
    for number in numbers:
        if number.startswith(oxygen):
            if number[i] == "1":
                count_o += 1
            lines_o += 1
        if number.startswith(co2):
            if number[i] == "1":
                count_c += 1
            lines_c += 1
    if lines_o > 1:
        if count_o >= lines_o // 2 + lines_o % 2:
            oxygen += "1"
        else:
            oxygen += "0"
    elif lines_o == 1:
        if count_o == 1:
            oxygen += "1"
        else:
            oxygen += "0"
    if lines_c > 1:
        if count_c < lines_c // 2 + lines_c % 2:
            co2 += "1"
        else:
            co2 += "0"
    elif lines_c == 1:
        if count_c == 1:
            co2 += "1"
        else:
            co2 += "0"

print(oxygen, int(oxygen, 2))
print(co2, int(co2, 2))

print(int(oxygen, 2) * int(co2, 2))
