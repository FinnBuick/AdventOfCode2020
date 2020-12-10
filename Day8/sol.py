import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve(inst_list):
    visited = set()
    hasLoop = False
    acc = i = 0
    while i < len(inst_list):
        if i in visited:
            hasLoop = True
            break

        visited.add(i)
        inst, num = inst_list[i]
        num = int(num)

        if inst == "nop":
            i += 1
            continue
        elif inst == "acc":
            acc += num
            i += 1
            continue
        elif inst == "jmp":
            i += num
            continue
    return (acc, hasLoop)


with open("input.txt", "r") as f:
    data = f.read()
    inst_list = [x.split() for x in data.split("\n")]

# s = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""
# print(solve(s))
print(solve(inst_list)[0])

swapDict = {"jmp": "nop", "nop": "jmp"}
for i, (inst, num) in enumerate(inst_list):
    if inst == "nop" or inst == "jmp":
        swapped = [(swapDict[inst], num)]
        newList = inst_list[:i] + swapped + inst_list[i+1:]
        accVal, looped = solve(newList)
        if not looped:
            print(accVal)
