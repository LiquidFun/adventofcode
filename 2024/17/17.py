import re
a, b, c, *nums = map(int, re.findall(r"\d+", open(0).read()))

def compute(A=a, B=b, C=c, pointer=0):
    out = []
    while pointer < len(nums):
        num = nums[pointer+1]
        combo = {4:A, 5:B, 6:C}.get(num, num)
        match nums[pointer]:
            case 0: A = A // 2**combo
            case 1: B ^= num
            case 2: B = combo % 8
            case 3 if A != 0: pointer = num - 2
            case 4: B ^= C
            case 5: out.append(combo % 8)
            case 6: B = A // 2**combo
            case 7: C = A // 2**combo
        pointer += 2
    return out

print(*compute(), sep=",")

def find_A(A, at=15):
    if at == -1:
        print(A)
        exit(0)
    while True:
        if nums[at:] == compute(A)[at:]:
            find_A(A, at-1)
        A += 8**at
find_A(8**15)
