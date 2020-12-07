#!/usr/bin/env python3

with open("input.txt") as f:
    content = f.readlines()

    data = [int(x.strip()) for x in content]

    for i in range(len(data)):
        for j in range(i, len(data)):
            res = data[i] + data[j]
            if res == 2020:
                print("Part 1:", data[i] * data[j])

    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                res = data[i] + data[j] + data[k]
                if res == 2020:
                    print("Part 2:", data[i] * data[j] * data[k])
