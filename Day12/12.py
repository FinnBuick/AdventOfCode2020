with open('Day12/input.txt', 'r') as f:
    instructions = [l.strip() for l in f.read().split('\n')]

# Positive in x direction is east, Negative is west
# Postive in y is north, negative is south
# 0 degrees is north


def solve1():
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    dir_ = 1
    pos = [0, 0]
    for i in instructions:
        action = i[0]
        val = int(i[1:])
        if action == 'N':
            pos[1] += val
        elif action == 'S':
            pos[1] -= val
        elif action == 'E':
            pos[0] += val
        elif action == 'W':
            pos[0] -= val
        elif action == 'L':
            for _ in range(val//90):
                dir_ = (dir_+3) % 4
        elif action == 'R':
            for _ in range(val//90):
                dir_ = (dir_+1) % 4
        elif action == 'F':
            pos[0] += val*DX[dir_]
            pos[1] += val*DY[dir_]
    return pos


def solve2():
    wp = [10, 1]
    pos = [0, 0]
    for i in instructions:
        action = i[0]
        val = int(i[1:])
        if action == 'N':
            wp[1] += val
        elif action == 'S':
            wp[1] -= val
        elif action == 'E':
            wp[0] += val
        elif action == 'W':
            wp[0] -= val
        elif action == 'L':
            for _ in range(val//90):
                newY, newX = wp
                wp = [-newX, newY]
        elif action == 'R':
            for _ in range(val//90):
                newY, newX = wp
                wp = [newX, -newY]
        elif action == 'F':
            wx, wy = wp
            pos[0] += val*wx
            pos[1] += val*wy
    return pos


def manhattan_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


print(solve1())
print(manhattan_dist([0, 0], solve1()))
print(solve2())
print(manhattan_dist([0, 0], solve2()))
