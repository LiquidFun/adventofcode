import sys

nums = [*map(int, sys.stdin.readlines())]

def solve(distance):
    return sum(a < b for a, b in zip(nums, nums[distance:]))

print(solve(1))
print(solve(3))

    
