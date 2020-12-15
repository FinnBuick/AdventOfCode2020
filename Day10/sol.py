from functools import reduce

with open("Day10/input.txt", "r") as f:
    lines = f.readlines()
    nums = list(map(int, lines))
    nums.append(0)
    nums = sorted(nums)
    lastAdapter = nums[-1] + 3
    nums.append(lastAdapter)


def part_1(nums):
    diffs = [0] * len(nums)
    for i in range(1, len(nums)):
        diffs[i] = nums[i] - nums[i-1]
    print(diffs.count(1) * diffs.count(3))
    return diffs


DP = {}


def dp(i):
    if i == len(nums)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(nums)):
        if nums[j] - nums[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans


# print(reduce(lambda x, y: x*y, part_1(nums)))
print(dp(0))
