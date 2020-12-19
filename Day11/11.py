import copy

with open("Day11/input.txt", "r") as f:
    L = [list(l.strip()) for l in f.read().split("\n")]
    # for row in L:
    #     print("".join(row))


def step(grid):
    newgrid = []
    for row in range(len(L)):
        newrow = ""
        for col in range(len(L[0])):
            adjacents = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    # if 0 <= row + dx < len(grid) and 0 <= col + dy < len(grid[0]):
                    #     adjacents.append(grid[row + dx][col + dy])
                    i = 1
                    while 0 <= row+i*dx < len(grid) and 0 <= col+i*dy < len(grid[0]):
                        el = grid[row+i*dx][col+i*dy]
                        if el != ".":
                            adjacents.append(el)
                            break
                        i += 1
            # if seat is empty
            if grid[row][col] == "L" and "#" not in adjacents:
                newrow += "#"
            elif grid[row][col] == "#" and adjacents.count("#") >= 5:
                newrow += "L"
            else:
                newrow += grid[row][col]
        newgrid.append(newrow)
    return newgrid


grid = L
while True:
    nextgrid = step(grid)
    # print("="*80)
    # for row in nextgrid:
    #     print("".join(row))
    if nextgrid == grid:
        print("".join(grid).count("#"))
        break
    grid = nextgrid
