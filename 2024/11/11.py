lookup = {}

def duplicate(num):
    if num in lookup:
        return lookup[num]
    nums = [num]
    for i in range(25):
        new = []
        for n in nums:
            s = str(n)
            if n == 0:
                new.append(1)
            elif len(s) % 2 == 0:
                new.append(int(s[:len(s)//2]))
                new.append(int(s[len(s)//2:]))
            else:
                new.append(n * 2024)
        nums = new
    lookup[num] = nums
    return nums

def solve(nums, target, i=0, s=0):
    if i == target:
        return len(nums)
    return sum(solve(duplicate(n), target, i+25) for n in nums)

nums = [int(a) for a in input().split()]
print(solve(nums, 25))
print(solve(nums, 75))

