from collections import Counter

counts = Counter([int(a) for a in input().split()])

for i in range(75):
    for n, occ in list(counts.items()):
        if (l := len(str(n))) % 2 == 0:
            counts[n // 10**(l//2)] += occ
            counts[n % 10**(l//2)] += occ
        else:
            counts[n * 2024 or 1] += occ
        counts[n] -= occ
    if i in (24, 74):
        print(sum(counts.values()))
