import re
from sys import stdin
s1, s2 = 0, 0
digits1 = list("0123456789")
digits2 = "zero one two three four five six seven eight nine".split()
as_num  = lambda num: digits2.index(num) if num in digits2 else int(num)

for line in stdin.readlines():
    nums1 = [n[1] for n in re.finditer('(?=(' + '|'.join(digits1) + '))', line)]
    nums2 = [n[1] for n in re.finditer('(?=(' + '|'.join(digits1 + digits2) + '))', line)]
    s1 += as_num(nums1[0]) * 10 + as_num(nums1[-1]) if nums1 else 0
    s2 += as_num(nums2[0]) * 10 + as_num(nums2[-1]) if nums2 else 0
print(s1, s2, sep="\n")
