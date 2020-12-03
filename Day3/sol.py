from functools import reduce

with open("input.txt") as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]

def treesHit(right, down):
    x = y = 0
    trees = 0
    for i, row in enumerate(lines):
        x = i * right
        y = i * down
        if y <= len(lines) and lines[y][x % len(row)] == "#":
            trees += 1
    return trees

slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]
trees = []
for right, down in slopes:
    trees.append(treesHit(right, down))

print("Part 1:", treesHit(3, 1))
print("Part 2:", reduce(lambda x, y : x * y, trees))
