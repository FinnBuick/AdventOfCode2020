import itertools

nums = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    nums = list(map(int, lines))


def isSum(target, start, end):
    prev_nums = nums[start:end]

    for a, b in itertools.combinations(prev_nums, 2):
        if a + b == target:
            return True
    return False


def contiguous_set(target):
    for i in range(len(nums)):
        total = 0
        start = i
        while total < target:
            total += nums[i]
            if total == target:
                return nums[start:i]
            i += 1


ans = 0
i = prev = 25
while i < len(nums):
    if not isSum(nums[i], i-prev, i):
        ans = nums[i]
        print(nums[i])
    i += 1

cs = contiguous_set(ans)
print(min(cs) + max(cs))
