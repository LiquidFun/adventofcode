from collections import Counter

counts = Counter([int(a) for a in input().split()])

for i in range(75):
    for n, occ in list(counts.items()):
        if n == 0:
            counts[1] += occ
        elif len(s := str(n)) % 2 == 0:
            counts[int(s[:len(s)//2])] += occ
            counts[int(s[len(s)//2:])] += occ
        else:
            counts[n * 2024] += occ
        counts[n] -= occ
    if i in (24, 74):
        print(sum(counts.values()))
