from functools import reduce

with open("Day10/input.txt", "r") as f:
    lines = f.readlines()
    nums = list(map(int, lines))


def findDiffs(nums):
    nums = sorted(nums)
    nums.insert(0, 0)
    last = nums[-1] + 3
    nums.append(last)

    diffs = [0] * len(nums)
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        diffs[i] = diff
    return [diffs.count(1), diffs.count(3)]


print(reduce(lambda x, y: x*y, findDiffs(nums)))
