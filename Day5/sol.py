with open("input.txt") as f:
    boarding_passes = [x.strip() for x in f.read().split('\n')]


def getId(bp):
    row = bp[:7]
    col = bp[7:]

    # Find row number
    row = int(row.replace("F", "0").replace("B", "1"), 2)
    col = int(col.replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


ids = []
for p in boarding_passes:
    ids.append(getId(p))

max = max(ids)
print('Part 1: ', max)

for valid in range(max):
    if valid not in ids:
        if valid - 1 in ids and valid + 1 in ids:
            print('Part 2: ', valid)
