import re
s1, s2 = 0, 0
digits = "0|1|2|3|4|5|6|7|8|9|_|one|two|three|four|five|six|seven|eight|nine"
as_num = lambda num: digits.split('|').index(num) % 10

for line in open(0):
    nums1 = [as_num(n[1]) for n in re.finditer(f'(?=({digits[:20]}))', line) if n[1]]
    nums2 = [as_num(n[1]) for n in re.finditer(f'(?=({digits}))', line) if n[1]]
    s1 += nums1[0]*10 + nums1[-1] if nums1 else 0
    s2 += nums2[0]*10 + nums2[-1] if nums2 else 0
print(s1, s2, sep="\n")
