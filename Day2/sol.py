import re

with open("input.txt") as f:
    lines = f.readlines()

    count1 = 0
    count2 = 0

    for line in lines:
        match = re.findall(r'(\d+)-(\d+) ([a-z]): (\w*)', line)[0]
        lower = int(match[0])
        upper = int(match[1])
        letter = match[2]
        password = match[3]

        if lower <= password.count(letter) <= upper:
            count1 += 1

        if (password[lower-1] == letter) ^ (password[upper-1] == letter):
            count2 += 1

    print("Part 1", count1)
    print("Part 2", count2)
