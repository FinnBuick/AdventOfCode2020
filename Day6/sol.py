with open("input.txt") as f:
    # Split input into groups using double line break
    groups = [x for x in f.read().split("\n\n")]

total = 0
for group in groups:
    # Add the number of unique questions per group to total
    num = len(set(list(group.replace("\n", ""))))
    total += num

print("Part 1:", total)

total_two = 0
for group in groups:
    answers = group.split("\n")
    answers = [set(x) for x in answers]
    # find intersection of answers within each group and add to total
    total_two += len(set.intersection(*answers))

print("Part 2:", total_two)
